const data = Deno.readFileSync(new URL("./input.txt", import.meta.url));
const decoder = new TextDecoder("utf-8");

type File = {
  name: string;
  size: number;
};

type Directory = {
  name: string;
  size: number;
  children: (File | Directory)[];
};

const DISK_SIZE = 70000000;
const UPDATE_SIZE = 30000000;

const sizes: number[] = [];

const createDirectory = (name: string, input: Iterator<string>): Directory => {
  const dir: Directory = {
    name,
    size: 0,
    children: [],
  };

  while (true) {
    const { value: line, done = false } = input.next();
    if (done) {
      break;
    } else if (line === "$ ls" || line.startsWith("dir ")) {
      continue;
    } else if (line.startsWith("$ cd ")) {
      const path = line.replace("$ cd ", "");
      if (path === "..") {
        sizes.push(dir.size);
        return dir;
      } else {
        const child = createDirectory(path, input);
        dir.children.push(child);
        dir.size += child.size;
      }
    } else {
      const [sizeStr, name] = line.split(" ");
      const size = parseInt(sizeStr, 10);
      dir.children.push({ name, size });
      dir.size += size;
    }
  }

  sizes.push(dir.size);
  return dir;
};

const iterator = decoder.decode(data).split("\n").values();
const { value: line, done } = iterator.next();
if (done) {
  throw new Error("No input");
} else if (line !== "$ cd /") {
  throw new Error("Invalid input");
}
const root = createDirectory(
  "/",
  iterator,
);

const need = UPDATE_SIZE - (DISK_SIZE - root.size);

for (const size of sizes.sort((a, b) => a - b)) {
  if (size >= need) {
    console.log(size);
    break;
  }
}

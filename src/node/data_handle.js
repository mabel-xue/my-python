const fs = require("fs");
const path = require("path");
const http = require("http");

const filePath = path.join(__dirname, "data.json");
const server = http.createServer((req, res) => {
  if (req.url === "/api/data") {
    // 读取 JSON 文件内容
    fs.readFile(filePath, "utf8", (err, data) => {
      if (err) {
        res.writeHead(500, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: err }));
        return;
      }

      try {
        const jsonData = JSON.parse(data).data.data.map((i) => i.title);

        // 设置接口返回的内容类型为 JSON
        res.setHeader("Content-Type", "application/json");
        // 返回 JSON 数据
        res.end(JSON.stringify(jsonData));
      } catch (error) {
        res.writeHead(500, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ error: "Invalid JSON format" }));
      }
    });
  } else {
    res.writeHead(404, { "Content-Type": "application/json" });
    res.end(JSON.stringify({ error: "Not Found" }));
  }
});

server.listen(3030, () => {
  console.log("Server is running on port 3030");
});

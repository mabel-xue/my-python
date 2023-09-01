const express = require("express");
const axios = require("axios");

const app = express();
const port = process.env.PORT || 5500;

// 添加你的代理路由
app.get("/get-h-detail", async (req, res) => {
  try {
    // 向目标服务器发出请求
    const response = await axios.get(
      "https://hweb-hotel.huazhu.com/hotels/hotel/detail?checkInDate=2023-09-02&checkOutDate=2023-09-04&guestPerRoom=1&hotelId=9011010&roomCount=1"
    );

    // 将响应发送回客户端
    res.send(response.data);
  } catch (error) {
    console.error(error);
    res.status(500).send("Proxy error");
  }
});

app.listen(port, () => {
  console.log(`Proxy server listening on port ${port}`);
});

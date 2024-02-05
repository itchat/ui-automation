# UI Automation

## Framework

UI 部分框架采用了微软 Playwright

- 框架全自动元素检查等待，用户无需自行额外下载 Google Chrome 等主流浏览器驱动，直接在参数中指定 channel 即可
- 启动速度相比于 selenium 较快并且其 codegen 生成器支持录制操作行为后生成代码，与 selenium IDE 功能类似
- 相比于 selenium 额外封装了可能的多种定位方法，无需额外二次封装

## Design Pattern

POM 设计模式

- base
  - 封装断言方法，指定元素方法是否可见
  - 模拟人手输入方法
  - 断言元素是否被选中
  - 截图功能
  - 点击器封装
  - 打开网页
- data
  - 存放各模块 DDT 模式所需数据，更具模块需要自由定义格式字段
- page
  - 各模块元素存放在此文件夹，可用 playwright codegen 指令自动生成，现阶段定位方法只添加了两个，后期需补全
- testcase
  - 调试模块，方法根据 data 中的字段而言修改装饰器
- tools
  - 神经网络自动识别验证码、CSV 数据导入装饰器：手动 closure 闭包实现

## Optimization

框架依然有大量优化尚未完成，可自行探索学习

- 针对断言部分结合 pytest, 替代自行闭包实现的 csv reader 装饰器
- DDT 向 KDT 的转变学习
- 多 TAB 同时多线程异步操作不同的测试模块
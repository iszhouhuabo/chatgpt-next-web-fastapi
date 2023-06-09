<div align="center">
<img src="https://raw.githubusercontent.com/iszhouhuabo/ChatGPT-Next-Web/main/docs/images/icon.svg" alt="预览"/>

<h1 align="center">ChatGPT Next Web For FastAPI</h1>

一键免费部署你的私人 ChatGPT 网页应用。

[演示 前端 Demo](https://zhb.chatools.online/) / [演示 后台 Demo](https://chatgpt-next-web-fastapi.vercel.app/) / [反馈 Issues](https://github.com/iszhouhuabo/chatgpt-next-web-fastapi/issues)

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fiszhouhuabo%2Fchatgpt-next-web-fastapi&env=OPENAI_API_KEY&env=CODE&project-name=chatgpt-next-web-fastapi&repository-name=chatgpt-next-web-fastapi)

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/iszhouhuabo/chatgpt-next-web-fastapi)

![主界面](https://raw.githubusercontent.com/iszhouhuabo/ChatGPT-Next-Web/main/docs/images/cover.png)

</div>

## ChatGPT-Next-Web For Python FastApi

> 站在巨人的肩膀上 - `Yidadaa`
>
> 如果你觉得这个项目对你有帮助，并且情况允许的话，可以帮忙 Star 一下，总之非常感谢支持～

前端基于 `Yidadaa` 的 [ChatGPT-Next-Web](https://github.com/Yidadaa/ChatGPT-Next-Web)
二次开发而来，只做了稍微的修改（这样同步更新`Yidadaa`的代码和功能更加方便，不要重复造轮子），主要去掉了 `NodeJs`
的后台，代码文件：`ChatGPT-Next-Web`

将后端代码修改成 `Python` 呢，主要是为了降低后台工程师的开发成本；因为之后准备引入后台管理这块，`Python` 搞起来相对简单一点。

<br/>

## 关于 FastAPI

不用担忧 `Python` 的效率问题，因为基于 `fastapi` ，FastAPI 是一个现代、快速（高性能）的 Web 框架，用于构建 API。
> 它使用 Python 3.6+ 中的类型注释，以及 Python 3.7+ 中的异步语法，这使得代码易于阅读、维护和自动化测试。
> FastAPI 是基于 Starlette 框架构建的，因此它继承了 Starlette 的许多特性，如 WebSocket 支持、GraphQL 支持、高性能、基于标准
> Python 类型提示的自动文档生成等。
> FastAPI 还提供了一个简单易用的依赖注入系统，使得开发人员可以轻松地编写可维护和可测试的代码。它还支持 OpenAPI 和 JSON
> Schema 规范，可以自动生成 API 文档，并提供交互式 API 文档 UI。

据官方说，和 NodeJs/Go 的速度有的一拼，详细介绍可以查看官方： [FastAPI](https://fastapi.tiangolo.com)

<br/>

## 开发计划

- [x] 为每个对话设置系统 Prompt
- [x] 允许用户自行编辑内置 Prompt 列表
- [x] 预制角色：使用预制角色快速定制新对话
- [x] 分享为图片，分享到 ShareGPT 链接 

- [ ] 界面文字自定义
- [ ] OpenAI 密钥轮询
- [ ] 用户登录、账号管理
- [ ] 消息云同步

<br/>

## 开始使用

### Python fastapi 后端

1. 准备好你的 [OpenAI API Key](https://platform.openai.com/account/api-keys);
2. 点击右侧按钮开始部署：
   [![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/iszhouhuabo/chatgpt-next-web-fastapi&env=OPENAI_API_KEY&env=CODE&project-name=chatgpt-next-web&repository-name=chatgpt-next-web-fastapi)
   ，直接使用 Github 账号登录即可，记得在环境变量页填入 API Key 和[页面访问密码](#配置页面访问密码) CODE；
   > 目前使用 Vercel 部署，SSE 流没办法正常运作，会有事件循环问题；可能是 Vercel 的配置有问题，目前正在想办法解决中... 本地开发和Docker部署不受影响
3. 部署完毕后，即可开始使用；
4. （可选）[绑定自定义域名](https://vercel.com/docs/concepts/projects/domains/add-a-domain)：Vercel 分配的域名 DNS
   在某些区域被污染了，绑定自定义域名即可直连。

### ChatGPT-Next-Web 前端

> Wait ....

<br/>

## 环境变量

### `OPENAI_API_KEY` （必填项）

OpanAI 密钥，你在 openai 账户页面申请的 api key。

### `CODE` （可选）

访问密码，可选，可以使用逗号隔开多个密码。

### `HIDE_USER_API_KEY` （可选）

隐藏前端自定义 OpenAI 密钥，设置成 `1` ，使用者将不能使用自己的 OpenAI 密钥

### `PROXY_URL` （可选）

代理服务器，请选用能信任的提供者；否则可能有泄漏 OpenAI 密钥的风险

## 使用方法@Mingyu

以下是[**Wechat exercise step number modification微信步数修改**](https://github.com/Y-7-0101/STEPS)使用的详细步骤和说明。

### 1. Fork 仓库

首先，在仓库页面上点击右上角的 "Fork" 按钮，将该仓库 fork 到你的 GitHub 账户下。这将在你的账户下创建一个仓库副本，你可以在副本中进行修改而不影响原始仓库。

### 2. 配置 Secrets

在开始之前，你需要配置以下 Secrets 变量：

- `ACCOUNTS`: 账号列表，多个账号之间使用逗号分隔。
- `PASSWORDS`: 密码列表，与账号列表一一对应，使用逗号分隔。
- `MIN_STEPS`: 步数范围的最小值。
- `MAX_STEPS`: 步数范围的最大值。

以下是如何配置 Secrets 的步骤：

1. 进入你 fork 的仓库页面，点击上方的 "Settings" 选项卡。
2. 在左侧导航栏中点击 "Secrets"。
3. 点击 "New repository secret" 按钮。
4. 输入变量名和对应的值，然后点击 "Add secret"。

确保将所有需要的 Secrets 变量都配置好，这些变量将用于在 GitHub Actions 中运行步数修改脚本时进行身份验证和参数传递。

### 3. 添加定时任务

该仓库使用 GitHub Actions 来触发定时任务并自动运行步数修改脚本。默认情况下，定时任务设置为每天晚上八点五十运行一次。如果需要更改定时任务的执行时间，请按照下面的步骤进行修改。

1. 打开 `.github/workflows/main.yml` 文件。
2. 在 `schedule` 事件的 `cron` 字段中，修改 Cron 表达式以设置适合你的执行时间。

例如，要将定时任务更改为每天上午十点运行一次，你可以将 `cron` 字段的值修改为 `"0 10 * * *"`。

默认为`cron: '6 10 * * *'`。UTC时间上午10点6分运行即北京时间下午18点6分运行。

请参考 Cron 表达式的文档或使用在线 Cron 表达式生成器来生成你需要的定时任务表达式。

### 4. 运行步数修改脚本

GitHub Actions 将根据定时任务的设定，在指定的时间自动运行步数修改脚本。这个脚本会根据设置的范围随机生成步数，并使用提供的账号和密码进行登录和修改。

在每次定时任务运行后，你可以在 GitHub Actions 日志中查看步数修改的结果。GitHub Actions 的日志提供了详细的输出，包括每个账号的步数修改结果和请求响应。
<div style="width: 100%;">
  <img style="width: 100%; height: auto;" src="https://github.com/Y-7-0101/STEPS/assets/135582157/3fbc0187-9479-4f30-ad3b-49cea957d22b">
</div>

## 注意事项

- 请确保在使用时不要将敏感信息（如密码）直接暴露在日志中。
- 需要确保在修改步数时遵守相关服务的使用规则和法律法规。

请根据上述步骤进行操作，以使用并配置该仓库。如果你有任何问题或需要进一步的帮助，请随时提问。
[**@Mingyu**](https://t.me/ymyuuu)

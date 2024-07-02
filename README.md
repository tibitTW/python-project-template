# python-project-template

方便快速設定開發環境的 python 模板

## File Structure

- `pyproject.toml`: ruff config
- `pyrightconfig.json`: pyright config

## Editor Setup

### Zed

If want to use zed as editor, add the following configs in zed's `settings.json` (`~/.config/zed/settings.json` or press `Cmd` + `,`)

```json
"languages": {
    "Python": {
        "format_on_save": {
            "external": {
                "command": "bash",
                "arguments": [
                    "-c",
                    "ruff check --select=I --fix --stdin-filename {buffer_path} | ruff format --stdin-filename {buffer_path}"
                ]
            }
        }
    }
},
```

# Godot Asset Library Deploy Action

## 📌 Description

This GitHub Action automatically updates your project in the [Godot Asset Library](https://godotengine.org/asset-library/) when a new release is created in your repository.

## ⚙️ How to Use

```yaml
name: Deploy to Godot Asset Library

on:
  release:
    types: [published]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Deploy to Godot Asset Library
        uses: talkafk/DeployGodotAssetLibraly@v1
        with:
          login: "your-login"
          password: ${{ secrets.GODOT_PASSWORD }}
          asset_id: "your-asset-id"
          commit_sha: ${{ github.sha }}
          release_tag: ${{ github.ref_name }}
```


## 🔧 Input Parameters

| Parameter     | Description                     | Required |
|--------------|---------------------------------|----------|
| `username`   | Godot Asset Library login      | ✅        |
| `password`   | Godot Asset Library password   | ✅        |
| `release_tag` | Release tag (e.g., `1.0.0`)    | ✅        |
| `commit_sha`  | Release commit SHA            | ✅        |

## 🔑 Secrets

Before using, create secret variable in your repository settings (`Settings` → `Secrets and variables` → `Actions` → `New repository secret`):

- `GODOT_PASSWORD` – your Godot Asset Library password

## 📜 License

This project is distributed under the MIT License.

## Usage

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


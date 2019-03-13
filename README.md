
# examples_python
python学習用

## 前提

- pyenv
- pipenv

## pipenvの使い方

### 仮想環境の作成
実はまだよく理解してないがgemとかnpmとかと思ってる

```bash
pipenv --python 3.7.2
```

### ライブラリの追加の仕方

```bash
pipenv install beautifulsoup4==4.6.0 requests==2.18.4
pipenv install --dev ipython==6.2.1 // --dev等で開発用も追加可能
```

## 参考URL
- [Pipenv で Python パッケージを管理する](https://qiita.com/QUANON/items/4a371651b07bb61fde41)
- [2018年のPythonプロジェクトのはじめかた](https://qiita.com/sl2/items/1e503952b9506a0539ea)
- [Mac上のPython仮想環境をpipenv+pyenvへ移行してみた](https://dev.classmethod.jp/etc/environment_to_pipenv-pyenv/)

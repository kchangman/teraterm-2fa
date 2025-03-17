# プロジェクト設定と注意事項

## 事前準備

以下の手順で環境を準備してください。
1. **リポジトリをクローンする**
   ```bash
   git clone https://github.com/kchangman/teraterm-2fa.git

2. ディレクトリに移動する
      ```bash
   git clone https://github.com/kchangman/teraterm-2fa.git

3. 仮想環境を作成する
   ```bash
   python -m venv hoge
   ```
   ※ 仮想環境名 `hoge` は任意の名前に変更可能ですが、  
   必ず `config.ttl` 内のPYTHON_VENVを編集してください：
   ```plain
   PYTHON_VENV = 'hoge'
   ```
   `hoge` の部分を仮想環境名に合わせて修正してください。

4. 実行ポリシーを変更する
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope Process
   ```

5. 仮想環境をアクティブ化する
   ```powershell
   hoge\Scripts\activate
   ```

6. 必要なパッケージをインストールする
   ```bash
   pip install pyotp
   ```
7. configファイルを編集する
   プロジェクト内にある config.ini,config.ttl  ファイルを編集し、環境に合わせて設定を調整してください。
---

## 注意事項

- スクリプト等が最後まで正常に実行されなかった場合、`otp_output.txt` ファイルが残る場合があります。
<br>この場合、**次回実行時にファイルへの書き込みができなくなる**可能性があります。
<br>必ず手動で `otp_output.txt` を削除してください。

---

## 現状の課題と改善点

### 現状課題

1. **`generate_otp.py` で出力した認証コードを `connect_host.ttl` で受け取る方法が分からない**
   - 対応策：
     - `.py` ファイルで一時テキストファイルを作成し、認証コードを書き込む。
     - `.ttl` ファイルで処理終了後に一時ファイルを削除する。

2. **複数ホストに対応したい**
   - 現状、`.ttl` ファイルに引数を渡す方法が分からないため、ホストの数だけ `.ttl` ファイルを用意する必要がある。

---

## 改善したい点

1. **`generate_otp.py` と `connect_host.ttl` 間のデータ受け渡し**
   - `generate_otp.py` で出力する認証コードを直接 `connect_host.ttl` で受け取る方法を調査する。
   - 一時的なテキストファイルを使用せず、より効率的な方法を模索する。

2. **複数ホストへの対応**
   - `.ttl` ファイルに引数を渡す方法を調査し、複数ホストに対応できるようにする。
   - ホストの数だけ `.ttl` ファイルを用意する必要がない方法を実現する。

---

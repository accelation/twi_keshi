# twi_keshi
(過去のツイートを)つい消しするスクリプト

## 使い方
* twitterの設定から「全ツイート履歴をリクエストする」で過去のツイートをダウンロードしてくる。
* download_file/data/js/tweets/ にyyyy_mm.jsのjsonファイルがあるので、ここから先頭行を取り除き、(READMEを参照してください)twi_list.jsにリネームし、スクリプトと同じディレクトリに置く。
* APIの制限上、一度に削除できる件数が限られているので、cronなどを使って定期的に回す。

## config.ini について
Consumer Keyなどについては、config.iniから取り出すようにしていて、
書式は以下のように設定しています。

```config.ini
[token]
CK = XXXXXXXXXXXXXXXXXXXXXX
CS = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
AT = XXXXXXXXX-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
AS = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 
```

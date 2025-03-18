# Vtuber_ChatBot-NLP-
 [しぐれうい](https://twitter.com/ui_shig)
さんの対話Botを作成しました。<Br>
[規約](https://uishig.fanbox.cc/posts/6268223)
# 概要<Br>
①形態素解析<Br>
②文字を受け取り、単語の分散表現(word2vec)を用いて単語を抽出する<Br>
③マルコフ連鎖（n=2）で文を生成<Br>
④Mastdonを用いて対話Botを作成<Br>
# 所感
Mastdon上で実装し、マルコフ連鎖をn=2、次元数を1000にしました。<Br>
# 実行結果
Mastodon上での出力です。右がチャットボットを用いて生成される言葉です。
  
<img src="https://user-images.githubusercontent.com/64608456/173075430-3c0e93ac-7ee7-47cb-8b9a-f166daab046a.png" alt="実行結果真" title="実行結果">

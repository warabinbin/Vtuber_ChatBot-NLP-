# Vtuber_ChatBot-NLP-
Vtuber：しぐれうい（https://twitter.com/ui_shig) さんの対話Botを作成しました。<Br>
# 機能<Br>
①形態素解析<Br>
②文字を受け取り、単語の分散表現(word2vec)を用いて単語を抽出する<Br>
③マルコフ連鎖（n=2）で文を生成<Br>
④Mastdon（twitterのようなもの）を用いて対話Botを作成<Br>
# 所感
Mastdon上で実装し、マルコフ連鎖をn=2、次元数を1000にしました。連鎖数、次元をあげることで精度が高くなりました。<Br>
# 実行結果
Mastodon上での出力です。
  
<img src="https://user-images.githubusercontent.com/64608456/173075430-3c0e93ac-7ee7-47cb-8b9a-f166daab046a.png" alt="実行結果真" title="実行結果">

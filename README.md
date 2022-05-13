# Vtuber_ChatBot-NLP-
Vtuber：しぐれうい（https://twitter.com/ui_shig) さんの対話Botを作成しました。<Br>
あいうえお<Br>
# 機能<Br>
①形態素解析<Br>
②文字を受け取り、単語の分散表現(word2vec)を用いて単語を抽出する<Br>
③マルコフ連鎖（n=1）で文を生成<Br>
④Mastdon（twitterのようなもの）を用いて対話Botを作成<Br>
# 所感
Umemiyaさん（https://qiita.com/Umemiya/items/027f8bac0650c28590b5）を参考にしました。<Br>
オリジナルな点としては、Mastdon上で実装したことで、苦戦した点はストリームデータ取得が上手くいかなかったことです。<Br>

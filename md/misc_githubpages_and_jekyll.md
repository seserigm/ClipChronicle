---
lang: ja-JP
title: GitHub Pages と Jekyll
---

わかんなくて何日か費やしたので未来の自分への手紙。

## GitHub Pages

GitHub に `\<ユーザ名\>.github.io` ってリポジトリを作ると、そのURLで公開できるよ。  
別名のリポジトリなら、`ユーザ名.github.io/\<リポジトリ名\>` ってURLで公開できるよ。

公開は、リポジトリの Settings - GitHub Pages で有効にできるよ。  
非公開は、リポジトリを削除すればできるよ。（有料会員ならプライベート化でもできる）

リポジトリのルートの README.md が index になるよ。  
リポジトリの構成のまま公開されるけど、md は utf-8 でも文字化けしたよ……。

テーマを適用させて、素のテキストじゃなく webページとして表示させれば文字化けしないし、見栄えも良くできるよ。
テーマは、リポジトリの Settings - GitHub Pages - Theme Chooser から選ぶと適用されるよ。

## Jekyll

テーマの適用には Jekyll っていう仕組みを使っているよ。  
困ったら Jekyll のドキュメントを読むといいよ。

GitHub Pages も Jekyll もリポジトリの外にある仕組みだから、変換後にどういう構成になったかはそれぞれの知識を持っていないと知るのが大変だよ。

Jekyll は mdファイルをラップする**だけ**の仕組みではないよ。  
Jekyll は（たぶん）mdファイルを html に変換して、GitHub Pagesサーバーに設置するよ。  
設定を書いて指定のパスで公開させたりもできるよ。

Jekyll に変換させたい md は、文書の先頭に front matter を記載しておくよ。  
front matter は `---` で括られたテキストで、記載する場合は必ず mdファイルの先頭に書くよ。

たとえば、mdディレクトリにある `about.md` を `ユーザ名.github.io/リポジトリ名/about` として公開したい場合は以下のように書くよ。

```yml
---
permalink: /about/
---
```

ここでは様々な情報を設定することができるよ。  
たとえば……

```yml
---
lang: ja-JP
permalink: /about/
title: 文書のタイトル
---
```

みたいに。  

一括で設定するには、_config.yml というファイルを編集するよ。  
_config.yml は、初回テーマ適用時にリポジトリのルートに追加されるよ。


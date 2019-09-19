---
lang: ja-JP
tags: GitHub Jekyll
---

# GitHub Pages と Jekyll

わかんなくてだいぶ時間を費やしたので未来の自分へのお手紙。
GitHubとリポジトリが何かを知っているくらいの前提です。

## GitHub Pages

GitHubに `<ユーザ名>.github.io`ってリポジトリを作ると、そのURLで公開できるよ。  
別名のリポジトリなら、`<ユーザ名>.github.io/<リポジトリ名>`ってURLで公開できるよ。

公開は、リポジトリのSettings - GitHub Pagesで有効にできるよ。  
非公開には、リポジトリを削除すればできるよ。
有料会員ならリポジトリのプライベート化もできるらしいよ。

リポジトリのルートにあるREADME.mdがindexになるよ。  
リポジトリの構成のまま公開されるけど、mdファイルはutf-8でも文字化けしたよ……。

テーマを適用させて、テキストじゃなくwebページとして表示させれば文字化けしないし、見栄えも良くできるよ。  
テーマは、リポジトリのSettings - GitHub Pages - Theme Chooserから選ぶと適用できるよ。

## Jekyll

テーマの適用にはJekyllっていう仕組みが使われているよ。  
困ったら[Jekyll公式のドキュメント](http://jekyllrb-ja.github.io/docs/github-pages/)を読むといいよ。  
読んでもわからなかったから自分はこれを書いているんだけど……。

GitHub PagesもJekyllもリポジトリの外にある仕組みだから、変換後にどういう構成になるかはそれぞれの知識を持っていないと知るのが大変だよ。

Jekyllは、mdファイルをラップする**だけ**の仕組みではないよ。  
自分はGitHubでmdを見たときのように、URLはmdファイルのもので見た目だけが変わると思っていたから躓きが大きかったよ……。

Jekyllは、mdファイルをhtmlに変換してGitHub Pagesサーバーに設置するよ。  
設定を書いて、指定のURLで公開させたりもできるよ。

変換させたいmdの先頭にはfront matterを記載するよ。  
front matterは`---`で括られたテキストブロックで、記載する場合は必ずmdファイルの先頭に書くよ。

たとえば、リポジトリ直下の`md`というディレクトリにある`about.md`を`ユーザ名.github.io/リポジトリ名/about`というURLで公開したい場合は以下のように書くよ。

```yml
---
permalink: /about/
---
```

permalinkを書いていないときは、`ユーザ名.github.io/リポジトリ名/md/about.html`というURLで公開されるよ。

このfront matterを使っていろんな情報を設定できるよ。  
たとえば……

```yml
---
lang: ja-JP
permalink: /githubpages-and-jekyll/
title: GitHub Pages と Jekyll
tags: GitHub Pages Jekyll
---
```

みたいに。  
逆に設定なしでhtml化したいときは、空のfront matterを置けばいいよ。

```yml
---
---
```

詳しくは[Jekyll公式のFront Matter](http://jekyllrb-ja.github.io/docs/front-matter/)を参照。

mdファイルごとにじゃなく一括で設定するには、_config.ymlというファイルを編集するよ。  
_config.ymlは、初回テーマ適用時にリポジトリのルートに追加されるよ。


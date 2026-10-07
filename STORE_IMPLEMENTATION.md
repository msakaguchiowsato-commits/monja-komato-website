# もんじゃ駒と 店舗ページ実装報告（ZIP v2反映）

## 1. 作成したファイル
- `stores/nakameguro/index.html`、`stores/higashi-gotanda/index.html`、`stores/nishi-gotanda/index.html`：静的店舗ページ。
- `data/stores.json`：店舗別データと共通の正式ドメイン設定。
- `data/assets.json`：完成版からの既存画像参照。
- `tools/build_stores.py`：共通テンプレートとページ生成処理。
- `assets/stores/stores.css`：店舗ページ専用レスポンシブCSS。
- `data/seo-report.json`：SEO・JSON-LDの完全な一覧。
- `STORE_IMPLEMENTATION.md`：本報告。
- ZIPから `monja_komato_home_final.html`、`monja_komato_menu_final.html` と `assets/` 内20画像を新規配置。

## 2. 変更したファイル
今回の更新：店舗別データ、画像参照、共通生成処理、店舗CSS、生成済み3ページ、SEO一覧、本報告。
完成版HTMLからの変更は以下のアンカー追加のみ。
- TOP：3店舗の既存カード見出しの店名を各店舗URLへのリンクに変更。
- メニュー：予約案内の既存文「中目黒・東五反田・西五反田からお選びください。」の3店名をそれぞれリンクに変更。
文章、既存CSS、レイアウト構造、画像参照を維持。メニューの追加リンクには既存の予約ボタン用CSSを継承しないためのインライン指定を付け、元の文の見た目を保っています。追加画像20ファイルはZIPとバイト単位で一致。

## 3. URL一覧
- `/stores/nakameguro/`
- `/stores/higashi-gotanda/`
- `/stores/nishi-gotanda/`

## /stores/nakameguro/：4–8. SEO情報
- title：中目黒のもんじゃ焼き・鉄板焼き・土日祝ランチ｜もんじゃ駒と 中目黒店
- H1：もんじゃ駒と 中目黒店
- meta description：中目黒駅徒歩2分、もんじゃ駒と 中目黒店。中目黒でもんじゃ焼き・鉄板焼きを楽しむなら。平日17:00〜23:00、土日祝12:00〜23:00。住所・電話予約・アクセス・メニューをご案内。カップルや家族でのお食事、初めてのもんじゃにも。
- canonical：TODO: 正式情報確認（正式ドメイン未定のためタグ未出力）
- OGP：type・locale・site_name・title・descriptionは出力済み。og:url・og:imageは正式ドメイン設定後に出力。
- Restaurant JSON-LD：

```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "もんじゃ駒と 中目黒店",
  "servesCuisine": [
    "もんじゃ焼き",
    "鉄板焼き"
  ],
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "東京都",
    "addressLocality": "目黒区",
    "streetAddress": "上目黒2-6-3 K&F中目黒 1F",
    "addressCountry": "JP"
  },
  "telephone": "03-6452-2345",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "https://schema.org/Monday",
        "https://schema.org/Tuesday",
        "https://schema.org/Wednesday",
        "https://schema.org/Thursday",
        "https://schema.org/Friday"
      ],
      "opens": "17:00",
      "closes": "23:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "https://schema.org/Saturday",
        "https://schema.org/Sunday"
      ],
      "opens": "12:00",
      "closes": "23:00"
    }
  ],
  "hasMap": "https://www.google.com/maps/search/?api=1&query=%E3%82%82%E3%82%93%E3%81%98%E3%82%83%E9%A7%92%E3%81%A8%20%E4%B8%AD%E7%9B%AE%E9%BB%92%20%E6%9D%B1%E4%BA%AC%E9%83%BD%E7%9B%AE%E9%BB%92%E5%8C%BA%E4%B8%8A%E7%9B%AE%E9%BB%922-6-3%20K%26F%E4%B8%AD%E7%9B%AE%E9%BB%92%201F",
  "sameAs": [
    "https://www.instagram.com/monja_komato/"
  ]
}
```

## /stores/higashi-gotanda/：4–8. SEO情報
- title：五反田のもんじゃ・鉄板焼き｜翌3時まで営業｜もんじゃ駒と 東五反田店
- H1：もんじゃ駒と 東五反田店
- meta description：五反田駅徒歩2分、もんじゃ駒と 東五反田店。毎日17:00〜翌3:00の深夜営業。五反田でもんじゃ・鉄板焼きや居酒屋を探す方へ、仕事帰りの飲み会・二軒目のお店選びに。住所・電話予約・Googleマップ・メニューをご案内。
- canonical：TODO: 正式情報確認（正式ドメイン未定のためタグ未出力）
- OGP：type・locale・site_name・title・descriptionは出力済み。og:url・og:imageは正式ドメイン設定後に出力。
- Restaurant JSON-LD：

```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "もんじゃ駒と 東五反田店",
  "servesCuisine": [
    "もんじゃ焼き",
    "鉄板焼き"
  ],
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "東京都",
    "addressLocality": "品川区",
    "streetAddress": "東五反田1-16-3 EAST-1ビル 1F",
    "addressCountry": "JP"
  },
  "telephone": "03-6277-3390",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "https://schema.org/Monday",
        "https://schema.org/Tuesday",
        "https://schema.org/Wednesday",
        "https://schema.org/Thursday",
        "https://schema.org/Friday",
        "https://schema.org/Saturday",
        "https://schema.org/Sunday"
      ],
      "opens": "17:00",
      "closes": "03:00"
    }
  ],
  "hasMap": "https://www.google.com/maps/search/?api=1&query=%E3%82%82%E3%82%93%E3%81%98%E3%82%83%E9%A7%92%E3%81%A8%20%E6%9D%B1%E4%BA%94%E5%8F%8D%E7%94%B0%20%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%93%81%E5%B7%9D%E5%8C%BA%E6%9D%B1%E4%BA%94%E5%8F%8D%E7%94%B01-16-3%20EAST-1%E3%83%93%E3%83%AB%201F",
  "sameAs": [
    "https://www.instagram.com/monja_komato_gotanda/"
  ]
}
```

## /stores/nishi-gotanda/：4–8. SEO情報
- title：西五反田・五反田のもんじゃ・ランチ｜もんじゃ駒と 西五反田店
- H1：もんじゃ駒と 西五反田店
- meta description：五反田駅徒歩5分、もんじゃ駒と 西五反田店。平日11:00〜14:00のランチと17:00〜23:00、土日祝12:00〜23:00に営業。西五反田・五反田でもんじゃや家族・グループのお食事を探す方へ、住所・電話予約・アクセスをご案内。
- canonical：TODO: 正式情報確認（正式ドメイン未定のためタグ未出力）
- OGP：type・locale・site_name・title・descriptionは出力済み。og:url・og:imageは正式ドメイン設定後に出力。
- Restaurant JSON-LD：

```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "もんじゃ駒と 西五反田店",
  "servesCuisine": [
    "もんじゃ焼き",
    "鉄板焼き"
  ],
  "address": {
    "@type": "PostalAddress",
    "addressRegion": "東京都",
    "addressLocality": "品川区",
    "streetAddress": "西五反田2-12-15 リーラハイタウン 1F",
    "addressCountry": "JP"
  },
  "telephone": "03-6417-3302",
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "https://schema.org/Monday",
        "https://schema.org/Tuesday",
        "https://schema.org/Wednesday",
        "https://schema.org/Thursday",
        "https://schema.org/Friday"
      ],
      "opens": "11:00",
      "closes": "14:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "https://schema.org/Monday",
        "https://schema.org/Tuesday",
        "https://schema.org/Wednesday",
        "https://schema.org/Thursday",
        "https://schema.org/Friday"
      ],
      "opens": "17:00",
      "closes": "23:00"
    },
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": [
        "https://schema.org/Saturday",
        "https://schema.org/Sunday"
      ],
      "opens": "12:00",
      "closes": "23:00"
    }
  ],
  "hasMap": "https://www.google.com/maps/search/?api=1&query=%E3%82%82%E3%82%93%E3%81%98%E3%82%83%E9%A7%92%E3%81%A8%20%E8%A5%BF%E4%BA%94%E5%8F%8D%E7%94%B0%20%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%93%81%E5%B7%9D%E5%8C%BA%E8%A5%BF%E4%BA%94%E5%8F%8D%E7%94%B02-12-15%20%E3%83%AA%E3%83%BC%E3%83%A9%E3%83%8F%E3%82%A4%E3%82%BF%E3%82%A6%E3%83%B3%201F",
  "sameAs": [
    "https://www.instagram.com/monja_komato_nishigotanda/"
  ]
}
```

## 9. 内部リンク
TOP・メニューから3店舗へ直接リンク。店舗ページからTOP・メニューと他の2店舗へリンク。パンくずはTOP→現在の店舗。
全5ページのローカルリンクと参照画像、ページ内アンカーの到達を確認。

## 10. TODO一覧
ページ上の不明項目は `TODO: 正式情報確認` と表示。
- 共通：公式ドメイン（ユーザー確認済み：現在未定）。canonical・og:url・og:image・構造化データURLは未出力。正式ドメイン決定後に一括反映。
- 全店舗：オンライン予約URL、電話予約の受付条件・受付時間、定休日、ラストオーダー、臨時休業・祝日の個別日程、最終入店時刻。
- 全店舗：正確なGoogleマップ店舗ピン・Place ID。現時点では完成版のGoogleマップ検索リンクと、店名・確認済み住所による検索地図を使用。Google上の登録情報は独立確認していません。
- 全店舗：撮影店舗を特定できる外観・内観写真、店舗別の人気メニュー・提供内容・価格・人気順位。撮影店舗不明の写真を特定店舗の写真と断定していません。
- 中目黒：ランチ限定メニュー、店舗での焼き方対応、子ども連れ対応・設備。
- 東五反田：飲み会予約・座席条件、遅い時間の入店可否。
- 西五反田：ランチ限定メニュー、グループ席・席数・貸切条件、家族予約条件・設備。

住所・電話番号・営業時間・最寄駅アクセス・Instagramは、ユーザー指定の完成版TOPの `#shop-information` に基づいて反映済み。FAQの営業時間と駅からのアクセスは確認済みの回答を掲載。土日祝営業時間は本文に明記。JSON-LDは通常曜日の営業時間を構造化し、祝日の日付別例外は未確認のため創作していません。東五反田の17:00–翌03:00は開店17:00・閉店03:00で表現。

## 再生成と4店舗目の追加
リポジトリで `python3 tools/build_stores.py` を実行。4店舗目は `data/stores.json` のstores配列に既存の店舗レコードを参考に新規レコードを追加し、固有のslug・名称・SEO・FAQ・店舗情報を入力。未確認情報はnull。サイト内他店舗リンクは自動更新されます。TOP・メニューのリンクは既存デザインに沿って別途追加してください。

正式ドメインが決まったら `site_url` にHTTPSの公式originを入力（末尾以外のパスなし）して再生成。canonical・og:url・og:image・Restaurantのurl/@id・BreadcrumbList JSON-LDが一括出力されます。店舗写真未設定時のOGP画像は既存ロゴ。実サイトの設定に架空ドメインは保存していません。ドメイン差し替えは使い捨ての隔離ディレクトリで検証済み。

## 検証結果
- 3店舗＋完成版TOP・メニュー：HTTP 200、ローカルリンク・参照画像・アンカーの到達。
- 3店舗：H1各1個、固有title/description、JSON-LD解析、住所・電話・曜日別営業時間。
- Chromium：390px / 1280px、全3店舗で横はみ出しなし、画像表示、FAQ開閉、電話CTAを確認。
- 完成版TOP・メニュー：表示文章・既存CSS・画像参照の同一性と、20画像のバイト単位一致を確認。390px / 1280pxでリンクを追加した店名見出し・メニュー予約案内文の幅・高さの差が1px未満、色・フォントが元HTMLと一致。
- 再生成の同一性と、隔離ディレクトリでのドメイン設定反映を確認。
- Googleマップ外部iframeはブラウザのレイアウト検証では差し替えており、Googleの応答・位置精度は未検証。実機スマートフォン、Googleリッチリザルト、公開先のSEO/MEO効果は未検証。

## 開発環境
Python 3標準ライブラリのみ使用。追加依存・資格情報は不要。
`cd /workspace/monja-komato-website` で `python3 -m http.server 8000 --bind 0.0.0.0` を実行。
起動手順は環境設定のstart_skillに保存。設定保存は公開操作ではありません。

## ルートTOP対応
ルートに `index.html` を追加。互換用 `monja_komato_home_final.html` とバイト単位で同一の内容です。店舗ページのヘッダーロゴとパンくずのTOPリンクは `/` に統一し、共通生成処理とドメイン設定後のパンくず構造化データも対応済み。

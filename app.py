import streamlit as st

st.title("ジャンル別アニメ・漫画＆競馬紹介アプリ")
st.write("左のサイドバーから好きなジャンルを選んでください")

# ===== データ定義 =====
anime_data = [
    {
        "title": "ドラゴンボール",
        "genres": ["アクション・バトル"],
        "image": "DB表紙.jpg",
        "scores": 5.0,
        "source": "出典：鳥山明『ドラゴンボール』42巻 表紙（集英社）"
    },
    {
        "title": "NARUTO",
        "genres": ["アクション・バトル"],
        "image": "NARUTO表紙.jpg",
        "scores": 4.5,
        "source": "出典：岸本斉史『NARUTO -ナルト-』1巻 表紙（集英社）"
    },
    {
        "title": "BLEACH",
        "genres": ["アクション・バトル"],
        "image": "BLEACH表紙.jpg",
        "scores": 4.0,
        "source": "出典：久保帯人『BLEACH』1巻 表紙（集英社）"
    },
    {
        "title": "ONE PIECE",
        "genres": ["アクション・バトル", "ファンタジー"],
        "image": "ONEPIECE表紙.jpg",
        "scores": 4.1,
        "source": "出典：尾田栄一郎『ONE PIECE』1巻 表紙（集英社）"
    },
    {
        "title": "呪術廻戦",
        "genres": ["アクション・バトル"],
        "image": "呪術廻戦表紙.jpg",
        "scores": 5.0,
        "source": "出典：芥見下々『呪術廻戦』29巻 表紙（集英社）\n出典：芥見下々『呪術廻戦』30巻 表紙（集英社）"
    },
    {
        "title": "Re:ゼロから始める異世界生活",
        "genres": ["ファンタジー"],
        "image": "リゼロ表紙.jpg",
        "scores": 4.8,
        "source": "出典：長月達平・大塚真一郎『Re:ゼロから始める異世界生活』1巻 表紙（KADOKAWA）"
    },
    {
        "title": "けいおん！",
        "genres": ["日常系"],
        "image": "けいおん表紙.jpg",
        "scores": 4.0,
        "source": "出典：かきふらい『けいおん！』1巻 表紙（芳文社）"
    },
    {
        "title": "日常",
        "genres": ["日常系", "ギャグ・コメディ"],
        "image": "日常表紙.jpg",
        "scores": 4.2,
        "source": "出典：あらゐけいいち『日常』1巻 表紙（角川書店）"
    },
    {
        "title": "ゆるキャン△",
        "genres": ["日常系"],
        "image": "ゆるきゃん表紙.jpg",
        "scores": 4.2,
        "source": "出典：あfろ『ゆるキャン△』1巻 表紙（芳文社）"
    },
    {
        "title": "ぼっち・ざ・ろっく！",
        "genres": ["日常系"],
        "image": "ぼざろ表紙.jpg",
        "scores": 4.2,
        "source": "出典：はまじあき『ぼっち・ざ・ろっく！』1巻 表紙（芳文社）"
    },
    {
        "title": "この素晴らしい世界に祝福を！",
        "genres": ["ファンタジー","ギャグ・コメディ"],
        "image": "このすば表紙.jpg",
        "scores": 4.1,
        "source": "出典：暁なつめ・三嶋くろね『この素晴らしい世界に祝福を！』1巻 表紙（KADOKAWA）"
    },
    {
        "title": "のんのんびより",
        "genres": ["日常系"],
        "image": "のんのん表紙.jpg",
        "scores": 4.1,
        "source": "出典：あっと『のんのんびより』1巻 表紙（KADOKAWA）"
    },
    {
        "title": "無職転生 ～異世界行ったら本気だす～",
        "genres": ["ファンタジー", "異世界"],
        "image": "無職転生表紙.jpg",
        "scores": 4.9,
        "source": "出典：理不尽な孫の手・シロタカ『無職転生 ～異世界行ったら本気だす～』1巻 表紙（KADOKAWA）"
    },
    {
        "title": "転生したらスライムだった件",
        "genres": ["ファンタジー", "異世界"],
        "image": "転スラ表紙.jpg",
        "scores": 4.1,
        "source": "出典：伏瀬・みっつばー『転生したらスライムだった件』1巻 表紙（講談社）"
    },
    {
        "title": "オーバーロード",
        "genres": ["ファンタジー", "異世界"],
        "image": "オーバーロード表紙.jpg",
        "scores": 4.0,
        "source": "出典：丸山くがね・so-bin『オーバーロード』1巻 表紙（KADOKAWA）"
    },
    {
        "title": "銀魂",
        "genres": ["アクション・バトル", "ギャグ・コメディ", "SF","ホラー","サスペンス","ラブコメ","ミステリー","心理戦"],
        "image": "銀魂表紙.jpg",
        "scores": 4.9,
        "source": "出典：空知英秋『銀魂』77巻 表紙（集英社）"
    },
    {
        "title": "STEINS;GATE",
        "genres": ["SF", "ホラー","サスペンス"],
        "image": "シュタゲ表紙.jpg",
        "scores": 4.4,
        "source": "出典：5pb.×ニトロプラス『STEINS;GATE』表紙"
    },
    {
        "title": "サマータイムレンダ",
        "genres": ["SF", "ホラー","サスペンス", "ミステリー"],
        "image": "サマータイムレンダ表紙.jpg",
        "scores": 4.8,
        "source": "出典：田中靖規『サマータイムレンダ』1巻 表紙（集英社）"
    },
    {
        "title": "亜人",
        "genres": ["SF", "サスペンス", "ホラー"],
        "image": "亜人表紙.jpg",
        "scores": 4.8,
        "source": "出典：桜井画門『亜人』1巻 表紙（講談社）"
    },
    {
        "title": "モブサイコ100",
        "genres": ["SF", "アクション・バトル", "ギャグ・コメディ"],
        "image": "モブサイコ表紙.jpg",
        "scores": 4.8,
        "source": "出典：ONE『モブサイコ100』1巻 表紙（小学館）"
    },
    {
        "title": "からかい上手の高木さん",
        "genres": ["ラブコメ", "日常系"],
        "image": "高木さん表紙.jpg",
        "scores": 4.8,
        "source": "出典：山本崇一朗『からかい上手の高木さん』1巻 表紙（小学館）"
    },
    {
        "title": "その着せ替え人形は恋をする",
        "genres": ["ラブコメ"],
        "image": "着せ恋表紙.jpg",
        "scores": 4.3,
        "source": "出典：福田晋一『その着せ替え人形は恋をする』1巻 表紙（スクウェア・エニックス）"
    },
    {
        "title": "CLANNAD",
        "genres": ["恋愛", "日常系", "感動"],
        "image": "クラナド表紙.jpg",
        "scores": 5.0,
        "source": "出典：Key『CLANNAD』表紙"
    },
    {
        "title": "かぐや様は告らせたい",
        "genres": ["ラブコメ", "ギャグ・コメディ","心理戦"],
        "image": "かぐやさま表紙.jpg",
        "scores": 4.0,
        "source": "出典：赤坂アカ『かぐや様は告らせたい～天才たちの恋愛頭脳戦～』1巻 表紙（集英社）"
    },
    {
        "title": "らんま1/2",
        "genres": ["ラブコメ", "ギャグ・コメディ", "アクション"],
        "image": "らんま表紙.jpg",
        "scores": 4.0,
        "source": "出典：高橋留美子『らんま1/2』1巻 表紙（小学館）"
    },
    {
        "title": "中二病でも恋がしたい！",
        "genres": ["ラブコメ", "日常系"],
        "image": "中二病表紙.jpg",
        "scores": 4.0,
        "source": "出典：虎虎・逢坂望美『中二病でも恋がしたい！』表紙（KADOKAWA）"
    },
    {
        "title": "とらドラ！",
        "genres": ["ラブコメ", "恋愛"],
        "image": "とらどら表紙.jpg",
        "scores": 4.1,
        "source": "出典：竹宮ゆゆこ・ヤス『とらドラ！』1巻 表紙（KADOKAWA）"
    },
    {
        "title": "負けヒロインが多すぎる！",
        "genres": ["ラブコメ"],
        "image": "負けヒロイン表紙.jpg",
        "scores": 4.2,
        "source": "出典：雨森たきび・いみぎむる『負けヒロインが多すぎる！』表紙（小学館）"
    },
    {
        "title": "ひぐらしのなく頃に",
        "genres": ["ホラー","サスペンス"],
        "image": "ひぐらし表紙.jpg",
        "scores": 4.2,
        "source": "出典：竜騎士07『ひぐらしのなく頃に』1巻 表紙（スクウェア・エニックス）"
    },
    {
        "title": "東京喰種",
        "genres": ["ホラー", "アクション・バトル"],
        "image": "東京グール表紙.jpg",
        "scores": 4.6,
        "source": "出典：石田スイ『東京喰種トーキョーグール』1巻 表紙（集英社）"
    },
    {
        "title": "寄生獣",
        "genres": ["SF", "ホラー"],
        "image": "寄生獣表紙.jpg",
        "scores": 4.7,
        "source": "出典：岩明均『寄生獣』1巻 表紙（講談社）"
    },
        {
        "title": "HUNTER×HUNTER",
        "genres": ["アクション・バトル", "ファンタジー"],
        "image": "ハンターハンター表紙.jpg",
        "scores": 4.3,
        "source": "出典：冨樫義博『HUNTER×HUNTER』1巻 表紙（集英社）"
    },
    {
        "title": "ハイキュー!!",
        "genres": ["スポーツ"],
        "image": "ハイキュー表紙.jpg",
        "scores": 4.9,
        "source": "出典：古舘春一『ハイキュー!!』1巻 表紙（集英社）"
    },
    {
        "title": "ブルーロック",
        "genres": ["スポーツ"],
        "image": "ブルーロック表紙.jpg",
        "scores": 4.6,
        "source": "出典：金城宗幸・ノ村優介『ブルーロック』1巻 表紙（講談社）"
    },
    {
        "title": "アイシールド21",
        "genres": ["スポーツ"],
        "image": "アイシールド21表紙.jpg",
        "scores": 4.2,
        "source": "出典：稲垣理一郎・村田雄介『アイシールド21』1巻 表紙（集英社）"
    },
    {
        "title": "SLAM DUNK",
        "genres": ["スポーツ"],
        "image": "スラムダンク表紙.jpg",
        "scores": 4.9,
        "source": "出典：井上雄彦『SLAM DUNK』1巻 表紙（集英社）"
    },
    {
        "title": "黒子のバスケ",
        "genres": ["スポーツ"],
        "image": "黒子のバスケ表紙.jpg",
        "scores": 4.1,
        "source": "出典：藤巻忠俊『黒子のバスケ』1巻 表紙（集英社）"
    },
    {
        "title": "DAYS",
        "genres": ["スポーツ"],
        "image": "DAYS表紙.jpg",
        "scores": 4.8,
        "source": "出典：安田剛士『DAYS』1巻 表紙（講談社）"
    },
    {
        "title": "MAJOR",
        "genres": ["スポーツ"],
        "image": "MAJOR表紙.jpg",
        "scores": 4.1,
        "source": "出典：満田拓也『MAJOR』1巻 表紙（小学館）"
    },
    {
        "title": "メダリスト",
        "genres": ["スポーツ"],
        "image": "メダリスト表紙.jpg",
        "scores": 4.2,
        "source": "出典：つるまいかだ『メダリスト』1巻 表紙（講談社）"
    },
    {
        "title": "DEATH NOTE",
        "genres": ["ミステリー", "サスペンス", "心理戦"],
        "image": "デスノート表紙.jpg",
        "scores": 4.1,
        "source": "出典：大場つぐみ・小畑健『DEATH NOTE』1巻 表紙（集英社）"
    },
    {
        "title": "氷菓",
        "genres": ["ミステリー", "日常系", "青春"],
        "image": "氷菓表紙.jpg",
        "scores": 4.0,
        "source": "出典：米澤穂信・タスクオーナ『氷菓』1巻 表紙（KADOKAWA）"
    },
    {
        "title": "名探偵コナン",
        "genres": ["ミステリー", "推理", "サスペンス"],
        "image": "コナン表紙.jpg",
        "scores": 3.9,
        "source": "出典：青山剛昌『名探偵コナン』1巻 表紙（小学館）"
    },
    {
        "title": "僕だけがいない街",
        "genres": ["ミステリー", "サスペンス", "SF"],
        "image": "僕街表紙.jpg",
        "scores": 4.2,
        "source": "出典：三部けい『僕だけがいない街』1巻 表紙（KADOKAWA）"
    }
]

keiba_data = [
    {
        "name": "オグリキャップ",
        "race": ["有馬記念（1990年）: ラストラン。奇跡の復活勝利で国民的名馬に",
                 "天皇賞（秋）（1988年）: 地方出身馬として初の天皇賞制覇",
                 "安田記念（1989年・1990年）:マイル王としての強さを証明（連覇）",
                 "マイルチャンピオンシップ（1989年）マイルGⅠ制覇",
                "ジャパンカップ（1989年）世界レベルでも通用する実力を示した"],
        "syasin": "オグリキャップ写真.jpg"
    }
]

genres = [
    "アクション・バトル",
    "ファンタジー",
    "日常系",
    "ギャグ・コメディ",
    "SF",
    "ラブコメ",
    "ホラー",
    "サスペンス",
    "スポーツ",
    "ミステリー",
    "心理戦"
]

main_page = st.sidebar.selectbox("メインジャンル",["","アニメ・漫画", "競馬"])

if main_page == "アニメ・漫画":

    page = st.sidebar.selectbox("ジャンル選択", [""] + genres)

    # ===== アニメ・漫画の表示処理 =====
    if page:
        st.title("アニメ・漫画のところ")
        st.header(page)

        for anime in anime_data:
            if page in anime["genres"]:
                st.subheader(anime["title"])
                st.image(anime["image"], width=350)
                st.write("ジャンル：" + " / ".join(anime["genres"]))
                st.write(f"評価：⭐ {anime['scores']}")
                st.caption(anime["source"])
        
           
if main_page == "競馬":
    
    # ===== アニメ・漫画の表示処理 =====
    for uma in keiba_data:
        st.subheader(uma["name"])
        st.image(uma["syasin"], width=350)
        st.markdown("**主なレース：**  \n" + "  \n".join(uma["race"]))
$VERSION_MAJOR = 0
$VERSION_SUFFIX = "a"
$VERSION_REVISION = (git rev-list HEAD --count)
$VERSION_HASH = (git log -1 --format=%H).Substring(0, 7)
$VERSION = "v${VERSION_MAJOR}.${VERSION_REVISION}${VERSION_SUFFIX}.${VERSION_HASH}"

# pack.mcmetaファイルを削除
if (Test-Path -Path "./pack.mcmeta") {
    Remove-Item -Path "./pack.mcmeta"
}

# テンプレートからpack.mcmetaファイルを作成
(Get-Content -Path "./pack.mcmeta.in") -replace "VERSION", $VERSION | Set-Content -Path "./pack.mcmeta"

# ZIPファイル名を定義
$zipFileName = "s3KmG${VERSION}.zip"

# すでに存在する同名ZIPを削除（念のため）
if (Test-Path -Path $zipFileName) {
    Remove-Item -Path $zipFileName
}

# zip.exeでZIPファイルを作成（カレントディレクトリ内のすべてのファイルとフォルダを含める）
& zip -r $zipFileName * -x $zipFileName

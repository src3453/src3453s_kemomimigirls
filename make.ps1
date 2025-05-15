# PowerShellバージョンのリソースパック作成スクリプト

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

# ZIPファイルの作成
$zipFileName = "s3KmG${VERSION}.zip"
Compress-Archive -Path "./assets/*", "./pack.png", "./pack.mcmeta" -DestinationPath $zipFileName -Force

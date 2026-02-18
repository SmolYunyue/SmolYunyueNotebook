param(
  [string]$Name = "main",
  [ValidateSet("main","sub")]
  [string]$Template = "main"
)

# repo 根目录 = scripts 的上一级
$repoRoot = Split-Path -Parent $PSScriptRoot

# 模板文件路径
$tplFile  = if ($Template -eq "sub") { "subtex_template.tex" } else { "maintex_template.tex" }
$tplPath  = Join-Path $repoRoot ("0_templates\{0}" -f $tplFile)

# 输出文件路径：创建在你当前所在目录
$dst = Join-Path (Get-Location) ("{0}.tex" -f $Name)

if (-not (Test-Path $tplPath)) { throw "Template not found: $tplPath" }
if (-not (Test-Path $dst)) { Copy-Item $tplPath $dst }

# 打开：如果 TeXworks 在 PATH 里就打开，否则只提示
if (Get-Command texworks -ErrorAction SilentlyContinue) {
  texworks $dst
} else {
  Write-Host "Created: $dst (TeXworks not found in PATH)"
}
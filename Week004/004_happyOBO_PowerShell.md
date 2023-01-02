### 레퍼런스 사이트

- 레퍼런스 사이트는 [https://learn.microsoft.com/en-us/powershell/module/cimcmdlets/?view=powershell-7.3][https://learn.microsoft.com/en-us/powershell/module/cimcmdlets/?view=powershell-7.3] 에서 접속할 수 있다.

### 주요 cmd

```ps1
# 파일의 해쉬 값을 반환한다. $Value.Hash 를 통해 접근할 수 있다.
Get-FileHash [Path] -Algorithm SHA256
# 해당 폴더 경로로 부터의 하위 폴더 / 경로 리스트 반환, -Recurse 파라미터가 붙으면 자식의 자식노드들까지 탐색한다.
Get-ChildItem -Path[-LiteralPath] -Recurse
# 경로 판단 및 분리시킬 때 유용한 cmd 값
Split-Path
# 해당 경로가 올바른 경로인지 판단
Test-Path
# 터미널 출력
Write-Host [PrintValue]
# 문자열 관련 cmd
$string.Split(",")
$string.Remove(startidx, count)
$string.Replace(origin, changed)
$string.Contains($substring)
```
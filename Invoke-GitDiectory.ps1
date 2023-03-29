function praseInfo($url) {
    $splitPath = $url -split "/" | Select-Object -Skip 3
    Write-Host $splitPath

    $info = @{}
    $info["author"] = "$($splitPath[0])"
    $info["repository"] = "$($splitPath[1])"
    $info["branch"] = "$($splitPath[3])"
    $info["type"] = "$($splitPath[2])"
    $info["path"] = "$($splitPath[$splitPath.Length - 2])/$($splitPath[$splitPath.Length - 1])"
    $info["diectory"] = $splitPath[$splitPath.Length - 1]
    $info["inputUrl"] = $url
    $info["rootUrl"] = ($splitPath[3])?
    "https://github.com/$($splitPath[0])/$($splitPath[1])/tree/$($splitPath[3])" :
    "https://github.com/$($splitPath[0])/$($splitPath[1])"

    return $info
}

function getInfoUrl($author, $repository, $path, $branch) {
    return  "https://api.github.com/repos/$($author)/$($repository)/contents/$($path)?ref=$($branch)"
}

function Invoke-GitDiectory($url) {
    Set-Location "~\downloads"
    $info = praseInfo $url
    $infoUrl = getInfoUrl $info["author"] $info["repository"] $info["path"] $info["branch"]

    if ($info["rootUrl"].Contains("tree") ) {
        New-Item -Force -ItemType "directory" -Path "./$($info["diectory"])" 
        Set-Location $info["diectory"]
    }
    else {
        New-Item -Force -ItemType "directory" -Path "./$($info["diectory"])"
        Set-Location $info["repository"]
    }

    # todo 遍歷資料夾並下載檔案
    # refreence https://github.com/MinhasKamal/DownGit/blob/master/app/home/down-git.js
    $res = (Invoke-WebRequest $infoUrl).Content | ConvertFrom-Json
    foreach ($item in $res) {
        if (!($item.type -eq "dir")) {
            $filepath = $item.download_url -split "/"
            Start-ThreadJob -Name $item.name -ScriptBlock {
                param($url, $filepath)
                Invoke-WebRequest -Uri $url -OutFile $filepath
            } -StreamingHost $Host -ArgumentList $item.download_url, "./$($filepath[$filename.Length - 1])"
        }
    }
}

Invoke-GitDiectory -url "https://github.com/plutov/packagemain/tree/master/16-wails-desktop-app/cpustats"
function praseInfo($url) {
    $splitPath = $url -split "/" | Select-Object -Skip 3
    Write-Host $splitPath

    $info = @{}
    $info["author"] = "$($splitPath[0])"
    $info["repository"] = "$($splitPath[1])"
    $info["branch"] = "$($splitPath[3])"
    $info["type"] = "$($splitPath[2])"
    $info["directory"] = "$($splitPath[$splitPath.Length - 1])"
    $info["diectory"] = $splitPath[$splitPath.Length - 1]
    $info["inputUrl"] = $url
    $info["rootUrl"] = ($splitPath[3])?
    "https://github.com/$($splitPath[0])/$($splitPath[1])/tree/$($splitPath[3])" :
    "https://github.com/$($splitPath[0])/$($splitPath[1])"

    return $info
}

function getInfoUrl($author, $repository, $branch) {
    return  "https://api.github.com/repos/$($author)/$($repository)/git/trees/$($branch)?recursive=1"
}

function getDownloadUrl($author, $repository, $branch, $path) {
    return  "https://raw.githubusercontent.com/$($author)/$($repository)/$($branch)/$($path)"
}

function iterDirectory($repoInfo, $files) {
    $infoUrl = getInfoUrl $repoInfo["author"] $repoInfo["repository"] $repoInfo["branch"]
    
    $res = $res = (Invoke-WebRequest $infoUrl).Content | ConvertFrom-Json
    $res = $res.tree | Where-Object { $_.path.Contains($repoInfo["directory"]) } | ForEach-Object {
        $item = $_
        $paths = $item.path -split "/"
        $path = ""
        if ([array]::IndexOf($paths, $repoInfo["directory"]) -eq 1) {
            $path = ($paths | Select-Object -Skip 1) -join "/"
        }
        else {
            $path = $paths -join "/"
        }

        if ($item.type -eq "tree") {
            New-Item -Force -ItemType "directory" -Path $path 
        }
        elseif ($item.type -eq "blob") {
            $dwUrl = getDownloadUrl $repoInfo["author"] $repoInfo["repository"] $repoInfo["branch"] $item.path
            Invoke-WebRequest -Uri $dwUrl -OutFile $path
            # Start-ThreadJob -ScriptBlock {
            #     param($url, $path)
            #     Invoke-WebRequest -Uri $dwUrl -OutFile $path
            # } -StreamingHost $Host -ArgumentList $dwUrl,$path
        }
    }
}

function Invoke-GithubDiectory($url) {
    Set-Location "~\downloads"
    $info = praseInfo $url

    if ($info["rootUrl"].Contains("tree") ) {
        New-Item -Force -ItemType "directory" -Path "./$($info["diectory"])" 
    }
    else {
        New-Item -Force -ItemType "directory" -Path "./$($info["diectory"])"
    }

    
    $files = @(@{
            Uri     = "";
            OutFile = "";
        })
    iterDirectory $info  $files
}

Invoke-GithubDiectory -url "https://github.com/plutov/packagemain/tree/master/16-wails-desktop-app/cpustats"
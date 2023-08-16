# Define the source and output directories
$SOURCE_DIR = "H:\Projects\GraphLinq\GraphLinq.Engine.Src"
$OUTPUT_DIR = "H:\Projects\GraphLinq\NodeBlock.Engine.Tests.Out"

# Get all the files recursively from the source directory
$files = Get-ChildItem -Path $SOURCE_DIR -Recurse -File

foreach ($file in $files) {
    # Determine the relative path for the file
    $relativePath = $file.FullName.Substring($SOURCE_DIR.Length)

    # Determine the output directory for the file based on its relative path
    $outputFileDir = Join-Path -Path $OUTPUT_DIR -ChildPath ([System.IO.Path]::GetDirectoryName($relativePath))

    # Ensure the output directory exists
    if (-not (Test-Path $outputFileDir)) {
        New-Item -ItemType Directory -Path $outputFileDir -Force
    }

    # Determine the output file name with 'Tests' suffix
    $outputFileName = $file.BaseName + "Tests" + $file.Extension
    $outputFilePath = Join-Path -Path $outputFileDir -ChildPath $outputFileName

    # Create the empty file with 'Tests' suffix in the output directory
    New-Item -ItemType File -Path $outputFilePath -Force
}

Write-Host "Done!"

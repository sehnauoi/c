require_once 'UnityAsset.php'; // This will require UnityBundle.php as it needs FileStream

$bundleFileName = 'bundle_name.unity3d'; // This is the bundle file with file header "UnityFS"
$bundleFileStream = new FileStream($bundleFileName); // Create a read stream
$assetsList = extractBundle($bundleFileStream); // This will extract assets to disk
unset($bundleFileStream); // Free the handle

foreach ($assetsList as $asset) {
  if (substr($asset, -4,4) == '.resS') continue; // .resS file is external data storage file
  $asset = new AssetFile($asset);

  foreach ($asset->preloadTable as &$item) {
    if ($item->typeString == 'Texture2D') {
      $item = new Texture2D($item, true); // Parse and read data
      $item->exportTo($item->name, 'webp', '-lossless 1'); // export to format, with additional encode parameters
      // $item->exportTo($item->name, 'png');
      unset($item); // Free up memory
    }
  }
  $asset->__desctruct();
  unset($asset); // Free up memory
}
foreach ($assetsList as $asset) {
  unlink($asset); // clean up files
}

# DearFlip PDF Flipbook for Laravel

A Laravel implementation of DearFlip PDF Flipbook viewer.

## Introduction

DearFlip is a powerful PDF Flipbook solution that offers a realistic book-like experience for viewing PDF documents on the web. This repository demonstrates how to integrate DearFlip with a Laravel application.

## Requirements

- PHP 8.1+
- Laravel 10.x
- jQuery (included with DearFlip)

## Installation

### 1. Download DearFlip

Purchase and download DearFlip from [official website](https://dearflip.com/).

### 2. Extract DearFlip Files

Extract the DearFlip package and copy the following directories to your Laravel public folder:

```bash
cp -r dflip/ /path/to/your/laravel/public/
```

Your directory structure should look like:

```
public/
├── dflip/
│   ├── css/
│   ├── js/
│   ├── sound/
│   └── images/
```

### 3. Add PDF Files

Place your PDF files in the public directory:

```bash
public/
├── pdf/
│   └── your-document.pdf
```

## Basic Usage

### 1. Include DearFlip Assets

In your Blade template (e.g., welcome.blade.php), include the required CSS and JavaScript files:

```html
<!-- DearFlip assets -->
<link rel="stylesheet" href="/dflip/css/dflip.min.css">
<script src="/dflip/js/libs/jquery.min.js"></script>
<script src="/dflip/js/dflip.js"></script>
```

### 2. Add the DearFlip Element

Add a container element where the PDF flipbook will be rendered:

```html
<div data-option="dflipOptions" class="df-element"></div>
```

### 3. Configure DearFlip Options

Set the DearFlip configuration in your controller and pass it to the view:

```php
// In your route or controller
$dflipOptions = [
    'source' => '/pdf/your-document.pdf'
];

return view('welcome', compact('dflipOptions'));
```

In your Blade template, initialize DearFlip with these options:

```html
<script>
    window.dflipLocation = "/dflip/";
    window.dflipOptions = @json($dflipOptions)
</script>
```

## Advanced Configuration

DearFlip offers many customization options. Here are some commonly used ones:

```php
$dflipOptions = [
    'source' => '/pdf/your-document.pdf',
    'height' => 800,                          // Height in pixels, or 'auto'
    'duration' => 800,                        // Page turn animation duration
    'backgroundColor' => "#FFFFFF",           // Background color
    'autoEnableOutline' => true,              // Auto show document outline
    'autoEnableThumbnail' => true,            // Auto show thumbnails
    'enableDownload' => true,                 // Enable PDF download
    'enableSound' => true,                    // Enable page flip sound
    'webgl' => true,                          // Use WebGL rendering
    'hard' => 'all',                          // Hard pages (none, cover, all)
    'openPage' => 1,                          // Initial page to open
    'pageMode' => 2,                          // 1=single, 2=double
    'singlePageMode' => 1,                    // 1=zoom, 2=booklet
];
```

## Event Callbacks

You can set callbacks for various events:

```php
$dflipOptions = [
    'source' => '/pdf/your-document.pdf',
    'onReady' => 'function(app) { console.log("DearFlip is ready!"); }',
    'onPageChanged' => 'function(app) { console.log("Page changed to: " + app.currentPageNumber); }',
    'onCreate' => 'function(app) { console.log("DearFlip created"); }',
];
```

## Multiple PDF Viewers

To have multiple PDF viewers on a single page:

```html
<div id="pdf1" class="df-element"></div>
<div id="pdf2" class="df-element"></div>

<script>
    $('#pdf1').flipBook('/pdf/document1.pdf', {
        height: 600,
        backgroundColor: "#FFC0CB"
    });
    
    $('#pdf2').flipBook('/pdf/document2.pdf', {
        height: 600,
        backgroundColor: "#ADD8E6"
    });
</script>
```

## Mobile Responsiveness

DearFlip is mobile-friendly. For best results on smaller screens, consider adjusting some settings:

```php
$dflipOptions = [
    'source' => '/pdf/your-document.pdf',
    'mobileViewMode' => 1,  // Force single page mode on mobile
];
```

## Troubleshooting

### PDF Not Loading

1. Check if the PDF path is correct
2. Ensure the PDF file is accessible (proper permissions)
3. Verify that all DearFlip assets are correctly loaded

### JavaScript Console Errors

Check the browser's console for any JavaScript errors, which may indicate:
- Missing DearFlip files
- jQuery conflicts
- PDF loading issues

## Additional Resources

- Official Documentation: [http://js.dearflip.com/docs](http://js.dearflip.com/docs)
- Support: [https://dearflip.com/support](https://dearflip.com/support)

## License

DearFlip requires a license purchase from [https://dearflip.com](https://dearflip.com).

This Laravel implementation example is for demonstration purposes.

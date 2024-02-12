// REF: https://blog.darkthread.net/blog/pdfium-core/

#r "nuget: System.Drawing.Common, 8.0.1"
#r "nuget: PDFiumCore, 122.0.6259"

using System.Drawing;
using System.Drawing.Imaging;
using PDFiumCore;

var scale = 1;
fpdfview.FPDF_InitLibrary();

var path = @"C:\Users\user\Desktop\各種履歷\109-111_score.pdf";
ExportImages(path, scale);

void ExportImages(string pdfPath, float scale)
{

    var imgFolder = Path.Combine(@"C:\Users\user\Downloads", Path.GetFileNameWithoutExtension(pdfPath));
    Directory.CreateDirectory(imgFolder);
    // 載入PDF
    var document = fpdfview.FPDF_LoadDocument(pdfPath, null);
    // 取得總頁數
    var pageCount = fpdfview.FPDF_GetPageCount(document);
    for (var pageIndex = 0; pageIndex < pageCount; pageIndex++)
    {
        // 逐頁載入
        var page = fpdfview.FPDF_LoadPage(document, pageIndex);
        
        // 取得尺寸，依比例縮放
        var size = new FS_SIZEF_();
        fpdfview.FPDF_GetPageSizeByIndexF(document, 0, size);

        var width = (int)Math.Round(size.Width * scale);
        var height = (int)Math.Round(size.Height * scale);

        var bitmap = fpdfview.FPDFBitmapCreateEx(
            width,
            height,
            (int)FPDFBitmapFormat.BGRA,
            IntPtr.Zero,
            0);
        
        // 填入白色背景
        fpdfview.FPDFBitmapFillRect(bitmap, 0, 0, width, height, (uint)Color.White.ToArgb());
        // |          | a b 0 |
        // | matrix = | c d 0 |
        // |          | e f 1 |
        using var matrix = new FS_MATRIX_();
        using var clipping = new FS_RECTF_();

        matrix.A = scale;
        matrix.B = 0;
        matrix.C = 0;
        matrix.D = scale;
        matrix.E = 0;
        matrix.F = 0;

        clipping.Left = 0;
        clipping.Right = width;
        clipping.Bottom = 0;
        clipping.Top = height;

        fpdfview.FPDF_RenderPageBitmapWithMatrix(bitmap, page, matrix, clipping, (int)RenderFlags.RenderAnnotations);
        
        //REF: https://stackoverflow.com/a/67744257/288936
        var bitmapImage = new Bitmap(
            width,
            height,
            fpdfview.FPDFBitmapGetStride(bitmap),
            PixelFormat.Format32bppArgb,
            fpdfview.FPDFBitmapGetBuffer(bitmap));

        bitmapImage.Save(
            Path.Combine(imgFolder, $"{pageIndex:000}.png"),
            ImageFormat.Png
        );
    }
}
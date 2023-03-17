#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>

#include "chessBoard/chessBoard.hpp"

cv::Mat src;

void opencvTest_onMouse(int event, int x, int y, int flags, void *)
{
    cv::Vec3b u = src.at<cv::Vec3b>(y, x);
    printf("(R,G,B)=(%d,%d,%d)\n", u.val[2], u.val[1], u.val[0]);
}

int opencvTest(bool getrgb)
{
    printf("%s\n", CV_VERSION);

    src = cv::imread("./images/Lenna.jpg");
    if (!src.data)
    {
        printf("Can't read the file\n");
        return -1;
    }

    cv::namedWindow("images/Lenna.jpg", 1);
    cv::imshow("images/Lenna.jpg", src);

    // 監聽滑鼠事件，執行對應callback
    // 這次的callback是顯示滑鼠指到的那一點的RGB號碼
    // 利用getrgb變數決定是否開啟
    if (getrgb)
    {
        cv::setMouseCallback("images/Lenna.jpg", opencvTest_onMouse, 0);
    }

    cv::waitKey(0);
    return 0;
}

int main()
{
    chessBoard();
    // opencvTest(!true);
    cv::destroyAllWindows();
    return 0;
}
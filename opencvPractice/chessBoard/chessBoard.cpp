#include "chessBoard.hpp"
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>

void chessBoard()
{
    cv::Mat src = cv::Mat::zeros(512, 512, CV_8UC1);
    int step = 512 / 8;
    bool toggle = true;
    for (int i = 0; i < 512; i += step)
    {
        for (int j = 0; j < 512; j += step)
        {
            cv::Scalar s = (toggle) ? cv::Scalar(0, 0, 0) : cv::Scalar(255, 255, 255);
            cv::rectangle(src, cv::Point(i, j), cv::Point(i + step, j + step), s, -1);
            toggle = !toggle;
        }
        toggle = !toggle;
    }

    cv::imshow("chess board", src);
    cv::waitKey(0);
}
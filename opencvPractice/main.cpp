#include <iostream>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include "chessBoard/chessBoard.hpp"


int opencvTest()
{
    std::cout << CV_VERSION << "\n";

    auto src = cv::imread("./images/Lenna.jpg");
    if (!src.data)
    {
        std::cout << "Can't read the file"
                  << "\n";
        return -1;
    }

    cv::namedWindow("images/Lenna.jpg", 1);
    cv::imshow("images/Lenna.jpg", src);

    cv::waitKey(0);
    return 0;
}

int main()
{
    chessBoard();
    // opencvTest();
    return 0;
}
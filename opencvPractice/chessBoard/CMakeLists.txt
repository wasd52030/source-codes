# 查找當目錄下的所有source file
# 並保存到 DIR_LIB_SRCS 變數
aux_source_directory(. DIR_LIB_SRCS)

# 先編譯成 dynamic link library，之後link到主程式上
add_library(chessBoard ${DIR_LIB_SRCS})
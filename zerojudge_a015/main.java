import java.util.*;

public class main {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int row, column;
        while (s.hasNext()) {
            row = s.nextInt();
            column = s.nextInt();
            int[][] A = new int[row][column];
            for (int i = 0; i < row; i++) {
                for (int j = 0; j < column; j++) {
                    A[i][j] = s.nextInt();
                }
            }

            for (int i = 0; i < column; i++) {
                for (int j = 0; j < row; j++) {
                    System.out.printf("%d ", A[j][i]);
                }
                System.out.println();
            }
        }
        s.close();
    }
}
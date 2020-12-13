import java.util.*;
public class s3A917045_1127_HW 
{
    static int maze[][];
    static int route[][];
    static int nowX = 1,nowY = 1;
    static int rtInd=0;
    public static void main(String[] args) 
    {
        Scanner num = new Scanner (System.in);
        System.out.print("請輸入迷宮的高跟寬(用空格隔開)=>");
        maze = new int[num.nextInt()+2][num.nextInt()+2]; //new added
        route = new int[10000][3];
        System.out.print("謝謝!已為你建立好含四周牆為["+maze.length+"*"+maze[0].length+"]的迷宮請輸入你希望迷宮中路佔總面積的百分比(0~100 int)=>");
        int ratio = num.nextInt();
        System.out.println("謝謝!已為你建立好含路:牆比為"+ratio+(":")+(100-ratio)+("的迷宮"));
        build(maze,ratio);
        print(maze);
        walk();
        num.close();
    }
    static void build(int[][]maze,int ratio)
    {
        for (int i = 1 ; i < maze.length ; i++)
        {
            for (int j = 1 ; j < maze[i].length ; j++)
            {
        		maze[i][j] = ((int)(Math.random()*10000)%100) < ratio ? 0 : 1;
        	}
        }
        for (int i = 0 ; i < maze.length ; i++)
        {
        	maze[i][0] = 1;
        	maze[i][maze[i].length-1] = 1;
        }
        for (int i = 0 ; i < maze[0].length ; i++)
        {
        	maze[0][i] = 1;
        	maze[maze.length-1][i] = 1;
        }
        maze[1][0] = 8;
        maze[maze.length-2][maze[0].length-1] = 9;
        maze[nowX][nowY] = 2;
        rtInd = 0 ;               //new added
        route[rtInd][0]=1;        //new added
        route[rtInd][1]=0;        //new added
        route[rtInd][2]=0;        //new added
        rtInd++;                  //new added
    }
    static void print(int[][]maze)
    {
        for (int[] row: maze)
        {
            System.out.print("\n");
            for (int col: row)
            {
                switch(col)
                {
                    case 0: System.out.print("  "); break;  //0=道路
                    case 1: System.out.print("██");  break; //1=牆壁 
                    case 2: System.out.print("@ "); break;  //2=老鼠當前位置
                    case 3: System.out.print("* "); break;  //3=走過必留下痕跡
                    case 5: System.out.print("=="); break;
                    case 8: System.out.print("8 "); break;  //8=起點
                    case 9: System.out.print("9 "); break;  //9=終點
                }
            }
        }
        System.out.print("\n");
    }
    static void walk()
    {
    	int nextX = nowX,nextY = nowY,nextWay = 0;
        while(maze[nowX][nowY] != 9 && rtInd >= 1 )//老鼠到終點前重複動作
        { 
            switch(nextWay)
            {
                case 0:                //右邊有路向右走
                    nextX = nowX;      
                    nextY = nowY + 1;
                    break;
                case 1:                //下面有路向下走
                    nextX = nowX + 1;  
                    nextY = nowY;
                    break;
                case 2:                //左邊有路向左走
                    nextX = nowX;      
                    nextY = nowY - 1;
                    break;
                case 3:                //上面有路向上走
                    nextX = nowX - 1;  
                    nextY = nowY;
                    break;
                case 4:
                    rtInd--;
                    maze[nowX][nowY] = 5 ; 
                    nowX = route[rtInd][0] ;
                    nowY = route[rtInd][1] ;
                    nextWay = route[rtInd][2] + 1 ;
                    maze[nowX][nowY] = 2 ;
                    print(maze);
                    continue; 
            }
            if(maze[nextX][nextY] == 0)  //如果老鼠前面一格有路
            {      
                maze[nowX][nowY] = 3;          //原地留下痕跡
                route[rtInd][0] = nowX ;
                route[rtInd][1] = nowY ;
                route[rtInd][2] = nextWay ;
                rtInd++;
                nowX = nextX;                  //往前移動
                nowY = nextY;
                maze[nowX][nowY] = 2;    
                print(maze);                   //畫迷宮
                nextWay = 0;                   //重置方向
            }
            else if(maze[nextX][nextY] == 9) //如果老鼠下一步為終點
            { 
                maze[nowX][nowY] = 3;          //原地留下痕跡
                nowX = nextX;                  //往前移動
                nowY = nextY;
                maze[nowX][nowY] = 2;
                print(maze);                   //畫迷宮
                System.out.println("老鼠走出迷宮了!");
                break;
            }
            else
            {
                nextWay++;                     //前方沒路就換方向
            }
        }
            if ( rtInd == 0 )
                System.out.println("這迷宮沒有出口"); 
    }
}

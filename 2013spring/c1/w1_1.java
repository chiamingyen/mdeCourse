
// Java 程式內容區分英文大小寫 w1_1 不可寫成 W1_1
// 而且程式檔案名稱必須與唯一的 public 類別名稱相同, 也就是檔案必須存為 w1_1.java
// 編譯執行本程式的方法, 在 Leo 編輯器中, 點選 @shadow c1/w1_1.java, 並以滑鼠右鍵選擇在 SciTe 中編輯
// 進入 SciTE 後, 以 Tools->Compile 執行編譯, 以 Tools->Go 執行程式
/*
public class w1_1 {
    public static void main(String[] args) {
        // 這裡所使用的中文編碼為 utf-8 編碼, 在編譯時必須特別指定
        System.out.println("開始學習 Java 程式語言!");
    }
}
*/
/*
import static java.lang.System.out;

public class w1_1 {
    public static void main(String[] args) {
       out.printf("%s! 開始學習 Java!%n", "準備好了");
    }
}
*/
/*
// 取得使用者的輸入
import java.util.Scanner;

public class w1_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("請輸入您的名字: ");
        System.out.printf("您好! %s!%n", scanner.next());
    }
}
*/
// 取得整數或浮點數
import java.util.Scanner;

public class w1_1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("請輸入一個整數: ");
        // 浮點數則使用 nextFloat(), 列印時則使用 %f
        System.out.printf("您所輸入的整數為 %d!%n", scanner.nextInt());
    }
}

package exemplo_atrib_obx;

public class Exemplo_atrib_obx {

    public static void main(String[] args) {
        Conta c1= new Conta("O de windows","8.8.8.8",100000000);
        System.out.println(c1.toString());
        Persoa p2= new Persoa("bbbbb","22222");
        Conta c2=new Conta(p2,5000);
        System.out.println(c2.toString());
    }
    
}

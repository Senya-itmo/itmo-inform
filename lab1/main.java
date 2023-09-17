public class main{
	public static void main(String[] args){
		long c = 10000000000l; // наше число в системе Фиб
		int a=0;  //наше число в десятичной системе

		int firstFibNum = 1; //Первое число в системе Фибонуччи
		int secondFibNum = 1; //Второе число в системе Фибонуччи
		int fibSum; //сумма 1 и 2 числа 

		while (c > 0){
			if (c % 10 == 1){ 
				a += secondFibNum;
			}

			fibSum = firstFibNum+secondFibNum;
			firstFibNum = secondFibNum;
			secondFibNum = fibSum; //получаем следующее число в системе Фибонуччи
			c /= 10;
		}

		System.out.printf("Ответ: %d", a); //Выводим ответ
	}
}
"""
Recur10. K sonining raqamlar yig’indisini takrorlanish operatoridan foydalanmagan
holda hisoblovchi butun toifadagi DigitSum(K) rekursiv funksiyasi tuzilsin. Shu
funksiya yordamida berilgan butun sonning raqamlari yig’indisi topilsin.
"""
def DigitSum(K):
    if K < 10:
        return K
    return K % 10 + DigitSum(K // 10)

print(DigitSum(13))

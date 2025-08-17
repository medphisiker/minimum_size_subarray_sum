from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """Функция возвращает минимальную длину подмассива в массиве `nums`,
        сумма которого больше или равна `target`.
        
        Используется паттерн sliding window с переменным размером окна.
        left - индекс элемента начала sliding window
        right - индекс элемента конца sliding window
        sliding window и есть подмассив, сумму элементов в котором мы отслеживаем.
        
        Если сумма чисел в sliding window < target - сдвигаем right вправо
        Если сумма чисел в sliding window >= target, то:
        1) обновляем минимальную длину подмассива
        2) сдвигаем left вправо, чтобы попытаться найти более короткий подмассив
        
        Временная сложность O(n) - в худшем случае оба указателя пройдут весь массив по одному разу.
        Пространственная сложность O(1) - память на доп. константы
        
        Args:
            target (int): порог по сумме элементов подмассива, который мы ищем
            nums (List[int]): массив положительных целых чисел

        Returns:
            int: минимальная длина подмассива, сумма которого больше или равна порогу `target`
        """
        left = 0
        window_sum = 0
        min_length = float('inf')
        
        # Двигаем правый указатель
        for right in range(len(nums)):
            window_sum += nums[right]
            
            # Пока сумма окна >= target, пытаемся уменьшить окно
            while window_sum >= target:
                min_length = min(min_length, right - left + 1)
                window_sum -= nums[left]
                left += 1
        
        # Если не нашли подходящего подмассива, возвращаем 0
        return 0 if min_length == float('inf') else min_length


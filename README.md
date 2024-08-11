# X進位乘法表(multiplication table of x carry)

舉例來說 Example:
```
2 二進位(bin):
1 × 1 =  1

3 三進位:
1 × 1 =  1  2 × 1 =  2
1 × 2 =  2  2 × 2 = 11

10 十進位(dec):
1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7  8 × 1 =  8  9 × 1 =  9
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 =  8  5 × 2 = 10  6 × 2 = 12  7 × 2 = 14  8 × 2 = 16  9 × 2 = 18
1 × 3 =  3  2 × 3 =  6  3 × 3 =  9  4 × 3 = 12  5 × 3 = 15  6 × 3 = 18  7 × 3 = 21  8 × 3 = 24  9 × 3 = 27
1 × 4 =  4  2 × 4 =  8  3 × 4 = 12  4 × 4 = 16  5 × 4 = 20  6 × 4 = 24  7 × 4 = 28  8 × 4 = 32  9 × 4 = 36
1 × 5 =  5  2 × 5 = 10  3 × 5 = 15  4 × 5 = 20  5 × 5 = 25  6 × 5 = 30  7 × 5 = 35  8 × 5 = 40  9 × 5 = 45
1 × 6 =  6  2 × 6 = 12  3 × 6 = 18  4 × 6 = 24  5 × 6 = 30  6 × 6 = 36  7 × 6 = 42  8 × 6 = 48  9 × 6 = 54
1 × 7 =  7  2 × 7 = 14  3 × 7 = 21  4 × 7 = 28  5 × 7 = 35  6 × 7 = 42  7 × 7 = 49  8 × 7 = 56  9 × 7 = 63
1 × 8 =  8  2 × 8 = 16  3 × 8 = 24  4 × 8 = 32  5 × 8 = 40  6 × 8 = 48  7 × 8 = 56  8 × 8 = 64  9 × 8 = 72
1 × 9 =  9  2 × 9 = 18  3 × 9 = 27  4 × 9 = 36  5 × 9 = 45  6 × 9 = 54  7 × 9 = 63  8 × 9 = 72  9 × 9 = 81
```


下面列出2到18進位乘法表(注意，這裡的18是十進位的，而不是16進位的):<br>
2 to 18 carry (Notice, "18" in here is decimal) :
```
1 × 1 =  1

1 × 1 =  1  2 × 1 =  2
1 × 2 =  2  2 × 2 = 11

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3
1 × 2 =  2  2 × 2 = 10  3 × 2 = 12
1 × 3 =  3  2 × 3 = 12  3 × 3 = 21

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4
1 × 2 =  2  2 × 2 =  4  3 × 2 = 11  4 × 2 = 13
1 × 3 =  3  2 × 3 = 11  3 × 3 = 14  4 × 3 = 22
1 × 4 =  4  2 × 4 = 13  3 × 4 = 22  4 × 4 = 31

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5
1 × 2 =  2  2 × 2 =  4  3 × 2 = 10  4 × 2 = 12  5 × 2 = 14
1 × 3 =  3  2 × 3 = 10  3 × 3 = 13  4 × 3 = 20  5 × 3 = 23
1 × 4 =  4  2 × 4 = 12  3 × 4 = 20  4 × 4 = 24  5 × 4 = 32
1 × 5 =  5  2 × 5 = 14  3 × 5 = 23  4 × 5 = 32  5 × 5 = 41

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 = 11  5 × 2 = 13  6 × 2 = 15
1 × 3 =  3  2 × 3 =  6  3 × 3 = 12  4 × 3 = 15  5 × 3 = 21  6 × 3 = 24
1 × 4 =  4  2 × 4 = 11  3 × 4 = 15  4 × 4 = 22  5 × 4 = 26  6 × 4 = 33
1 × 5 =  5  2 × 5 = 13  3 × 5 = 21  4 × 5 = 26  5 × 5 = 34  6 × 5 = 42
1 × 6 =  6  2 × 6 = 15  3 × 6 = 24  4 × 6 = 33  5 × 6 = 42  6 × 6 = 51

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 = 10  5 × 2 = 12  6 × 2 = 14  7 × 2 = 16
1 × 3 =  3  2 × 3 =  6  3 × 3 = 11  4 × 3 = 14  5 × 3 = 17  6 × 3 = 22  7 × 3 = 25
1 × 4 =  4  2 × 4 = 10  3 × 4 = 14  4 × 4 = 20  5 × 4 = 24  6 × 4 = 30  7 × 4 = 34
1 × 5 =  5  2 × 5 = 12  3 × 5 = 17  4 × 5 = 24  5 × 5 = 31  6 × 5 = 36  7 × 5 = 43
1 × 6 =  6  2 × 6 = 14  3 × 6 = 22  4 × 6 = 30  5 × 6 = 36  6 × 6 = 44  7 × 6 = 52
1 × 7 =  7  2 × 7 = 16  3 × 7 = 25  4 × 7 = 34  5 × 7 = 43  6 × 7 = 52  7 × 7 = 61

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7  8 × 1 =  8
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 =  8  5 × 2 = 11  6 × 2 = 13  7 × 2 = 15  8 × 2 = 17
1 × 3 =  3  2 × 3 =  6  3 × 3 = 10  4 × 3 = 13  5 × 3 = 16  6 × 3 = 20  7 × 3 = 23  8 × 3 = 26
1 × 4 =  4  2 × 4 =  8  3 × 4 = 13  4 × 4 = 17  5 × 4 = 22  6 × 4 = 26  7 × 4 = 31  8 × 4 = 35
1 × 5 =  5  2 × 5 = 11  3 × 5 = 16  4 × 5 = 22  5 × 5 = 27  6 × 5 = 33  7 × 5 = 38  8 × 5 = 44
1 × 6 =  6  2 × 6 = 13  3 × 6 = 20  4 × 6 = 26  5 × 6 = 33  6 × 6 = 40  7 × 6 = 46  8 × 6 = 53
1 × 7 =  7  2 × 7 = 15  3 × 7 = 23  4 × 7 = 31  5 × 7 = 38  6 × 7 = 46  7 × 7 = 54  8 × 7 = 62
1 × 8 =  8  2 × 8 = 17  3 × 8 = 26  4 × 8 = 35  5 × 8 = 44  6 × 8 = 53  7 × 8 = 62  8 × 8 = 71

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7  8 × 1 =  8  9 × 1 =  9
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 =  8  5 × 2 = 10  6 × 2 = 12  7 × 2 = 14  8 × 2 = 16  9 × 2 = 18
1 × 3 =  3  2 × 3 =  6  3 × 3 =  9  4 × 3 = 12  5 × 3 = 15  6 × 3 = 18  7 × 3 = 21  8 × 3 = 24  9 × 3 = 27
1 × 4 =  4  2 × 4 =  8  3 × 4 = 12  4 × 4 = 16  5 × 4 = 20  6 × 4 = 24  7 × 4 = 28  8 × 4 = 32  9 × 4 = 36
1 × 5 =  5  2 × 5 = 10  3 × 5 = 15  4 × 5 = 20  5 × 5 = 25  6 × 5 = 30  7 × 5 = 35  8 × 5 = 40  9 × 5 = 45
1 × 6 =  6  2 × 6 = 12  3 × 6 = 18  4 × 6 = 24  5 × 6 = 30  6 × 6 = 36  7 × 6 = 42  8 × 6 = 48  9 × 6 = 54
1 × 7 =  7  2 × 7 = 14  3 × 7 = 21  4 × 7 = 28  5 × 7 = 35  6 × 7 = 42  7 × 7 = 49  8 × 7 = 56  9 × 7 = 63
1 × 8 =  8  2 × 8 = 16  3 × 8 = 24  4 × 8 = 32  5 × 8 = 40  6 × 8 = 48  7 × 8 = 56  8 × 8 = 64  9 × 8 = 72
1 × 9 =  9  2 × 9 = 18  3 × 9 = 27  4 × 9 = 36  5 × 9 = 45  6 × 9 = 54  7 × 9 = 63  8 × 9 = 72  9 × 9 = 81

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7  8 × 1 =  8  9 × 1 =  9  ┴ × 1 =  ┴
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 =  8  5 × 2 =  ┴  6 × 2 = 11  7 × 2 = 13  8 × 2 = 15  9 × 2 = 17  ┴ × 2 = 19
1 × 3 =  3  2 × 3 =  6  3 × 3 =  9  4 × 3 = 11  5 × 3 = 14  6 × 3 = 17  7 × 3 = 1┴  8 × 3 = 22  9 × 3 = 25  ┴ × 3 = 28
1 × 4 =  4  2 × 4 =  8  3 × 4 = 11  4 × 4 = 15  5 × 4 = 19  6 × 4 = 22  7 × 4 = 26  8 × 4 = 2┴  9 × 4 = 33  ┴ × 4 = 37
1 × 5 =  5  2 × 5 =  ┴  3 × 5 = 14  4 × 5 = 19  5 × 5 = 23  6 × 5 = 28  7 × 5 = 32  8 × 5 = 37  9 × 5 = 41  ┴ × 5 = 46
1 × 6 =  6  2 × 6 = 11  3 × 6 = 17  4 × 6 = 22  5 × 6 = 28  6 × 6 = 33  7 × 6 = 39  8 × 6 = 44  9 × 6 = 4┴  ┴ × 6 = 55
1 × 7 =  7  2 × 7 = 13  3 × 7 = 1┴  4 × 7 = 26  5 × 7 = 32  6 × 7 = 39  7 × 7 = 45  8 × 7 = 51  9 × 7 = 58  ┴ × 7 = 64
1 × 8 =  8  2 × 8 = 15  3 × 8 = 22  4 × 8 = 2┴  5 × 8 = 37  6 × 8 = 44  7 × 8 = 51  8 × 8 = 59  9 × 8 = 66  ┴ × 8 = 73
1 × 9 =  9  2 × 9 = 17  3 × 9 = 25  4 × 9 = 33  5 × 9 = 41  6 × 9 = 4┴  7 × 9 = 58  8 × 9 = 66  9 × 9 = 74  ┴ × 9 = 82
1 × ┴ =  ┴  2 × ┴ = 19  3 × ┴ = 28  4 × ┴ = 37  5 × ┴ = 46  6 × ┴ = 55  7 × ┴ = 64  8 × ┴ = 73  9 × ┴ = 82  ┴ × ┴ = 91

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7  8 × 1 =  8  9 × 1 =  9  ┴ × 1 =  ┴  ┬ × 1 =  ┬
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 =  8  5 × 2 =  ┴  6 × 2 = 10  7 × 2 = 12  8 × 2 = 14  9 × 2 = 16  ┴ × 2 = 18  ┬ × 2 = 1┴
1 × 3 =  3  2 × 3 =  6  3 × 3 =  9  4 × 3 = 10  5 × 3 = 13  6 × 3 = 16  7 × 3 = 19  8 × 3 = 20  9 × 3 = 23  ┴ × 3 = 26  ┬ × 3 = 29
1 × 4 =  4  2 × 4 =  8  3 × 4 = 10  4 × 4 = 14  5 × 4 = 18  6 × 4 = 20  7 × 4 = 24  8 × 4 = 28  9 × 4 = 30  ┴ × 4 = 34  ┬ × 4 = 38
1 × 5 =  5  2 × 5 =  ┴  3 × 5 = 13  4 × 5 = 18  5 × 5 = 21  6 × 5 = 26  7 × 5 = 2┬  8 × 5 = 34  9 × 5 = 39  ┴ × 5 = 42  ┬ × 5 = 47
1 × 6 =  6  2 × 6 = 10  3 × 6 = 16  4 × 6 = 20  5 × 6 = 26  6 × 6 = 30  7 × 6 = 36  8 × 6 = 40  9 × 6 = 46  ┴ × 6 = 50  ┬ × 6 = 56
1 × 7 =  7  2 × 7 = 12  3 × 7 = 19  4 × 7 = 24  5 × 7 = 2┬  6 × 7 = 36  7 × 7 = 41  8 × 7 = 48  9 × 7 = 53  ┴ × 7 = 5┴  ┬ × 7 = 65
1 × 8 =  8  2 × 8 = 14  3 × 8 = 20  4 × 8 = 28  5 × 8 = 34  6 × 8 = 40  7 × 8 = 48  8 × 8 = 54  9 × 8 = 60  ┴ × 8 = 68  ┬ × 8 = 74
1 × 9 =  9  2 × 9 = 16  3 × 9 = 23  4 × 9 = 30  5 × 9 = 39  6 × 9 = 46  7 × 9 = 53  8 × 9 = 60  9 × 9 = 69  ┴ × 9 = 76  ┬ × 9 = 83
1 × ┴ =  ┴  2 × ┴ = 18  3 × ┴ = 26  4 × ┴ = 34  5 × ┴ = 42  6 × ┴ = 50  7 × ┴ = 5┴  8 × ┴ = 68  9 × ┴ = 76  ┴ × ┴ = 84  ┬ × ┴ = 92
1 × ┬ =  ┬  2 × ┬ = 1┴  3 × ┬ = 29  4 × ┬ = 38  5 × ┬ = 47  6 × ┬ = 56  7 × ┬ = 65  8 × ┬ = 74  9 × ┬ = 83  ┴ × ┬ = 92  ┬ × ┬ = ┴1

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7  8 × 1 =  8  9 × 1 =  9  ┴ × 1 =  ┴  ┬ × 1 =  ┬  ┤ × 1 =  ┤
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 =  8  5 × 2 =  ┴  6 × 2 =  ┤  7 × 2 = 11  8 × 2 = 13  9 × 2 = 15  ┴ × 2 = 17  ┬ × 2 = 19  ┤ × 2 = 1┬
1 × 3 =  3  2 × 3 =  6  3 × 3 =  9  4 × 3 =  ┤  5 × 3 = 12  6 × 3 = 15  7 × 3 = 18  8 × 3 = 1┬  9 × 3 = 21  ┴ × 3 = 24  ┬ × 3 = 27  ┤ × 3 = 2┴
1 × 4 =  4  2 × 4 =  8  3 × 4 =  ┤  4 × 4 = 13  5 × 4 = 17  6 × 4 = 1┬  7 × 4 = 22  8 × 4 = 26  9 × 4 = 2┴  ┴ × 4 = 31  ┬ × 4 = 35  ┤ × 4 = 39
1 × 5 =  5  2 × 5 =  ┴  3 × 5 = 12  4 × 5 = 17  5 × 5 = 1┤  6 × 5 = 24  7 × 5 = 29  8 × 5 = 31  9 × 5 = 36  ┴ × 5 = 3┬  ┬ × 5 = 43  ┤ × 5 = 48
1 × 6 =  6  2 × 6 =  ┤  3 × 6 = 15  4 × 6 = 1┬  5 × 6 = 24  6 × 6 = 2┴  7 × 6 = 33  8 × 6 = 39  9 × 6 = 42  ┴ × 6 = 48  ┬ × 6 = 51  ┤ × 6 = 57
1 × 7 =  7  2 × 7 = 11  3 × 7 = 18  4 × 7 = 22  5 × 7 = 29  6 × 7 = 33  7 × 7 = 3┴  8 × 7 = 44  9 × 7 = 4┬  ┴ × 7 = 55  ┬ × 7 = 5┤  ┤ × 7 = 66
1 × 8 =  8  2 × 8 = 13  3 × 8 = 1┬  4 × 8 = 26  5 × 8 = 31  6 × 8 = 39  7 × 8 = 44  8 × 8 = 4┤  9 × 8 = 57  ┴ × 8 = 62  ┬ × 8 = 6┴  ┤ × 8 = 75
1 × 9 =  9  2 × 9 = 15  3 × 9 = 21  4 × 9 = 2┴  5 × 9 = 36  6 × 9 = 42  7 × 9 = 4┬  8 × 9 = 57  9 × 9 = 63  ┴ × 9 = 6┤  ┬ × 9 = 78  ┤ × 9 = 84
1 × ┴ =  ┴  2 × ┴ = 17  3 × ┴ = 24  4 × ┴ = 31  5 × ┴ = 3┬  6 × ┴ = 48  7 × ┴ = 55  8 × ┴ = 62  9 × ┴ = 6┤  ┴ × ┴ = 79  ┬ × ┴ = 86  ┤ × ┴ = 93
1 × ┬ =  ┬  2 × ┬ = 19  3 × ┬ = 27  4 × ┬ = 35  5 × ┬ = 43  6 × ┬ = 51  7 × ┬ = 5┤  8 × ┬ = 6┴  9 × ┬ = 78  ┴ × ┬ = 86  ┬ × ┬ = 94  ┤ × ┬ = ┴2
1 × ┤ =  ┤  2 × ┤ = 1┬  3 × ┤ = 2┴  4 × ┤ = 39  5 × ┤ = 48  6 × ┤ = 57  7 × ┤ = 66  8 × ┤ = 75  9 × ┤ = 84  ┴ × ┤ = 93  ┬ × ┤ = ┴2  ┤ × ┤ = ┬1

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7  8 × 1 =  8  9 × 1 =  9  ┴ × 1 =  ┴  ┬ × 1 =  ┬  ┤ × 1 =  ┤  ├ × 1 =  ├
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 =  8  5 × 2 =  ┴  6 × 2 =  ┤  7 × 2 = 10  8 × 2 = 12  9 × 2 = 14  ┴ × 2 = 16  ┬ × 2 = 18  ┤ × 2 = 1┴  ├ × 2 = 1┤
1 × 3 =  3  2 × 3 =  6  3 × 3 =  9  4 × 3 =  ┤  5 × 3 = 11  6 × 3 = 14  7 × 3 = 17  8 × 3 = 1┴  9 × 3 = 1├  ┴ × 3 = 22  ┬ × 3 = 25  ┤ × 3 = 28  ├ × 3 = 2┬
1 × 4 =  4  2 × 4 =  8  3 × 4 =  ┤  4 × 4 = 12  5 × 4 = 16  6 × 4 = 1┴  7 × 4 = 20  8 × 4 = 24  9 × 4 = 28  ┴ × 4 = 2┤  ┬ × 4 = 32  ┤ × 4 = 36  ├ × 4 = 3┴
1 × 5 =  5  2 × 5 =  ┴  3 × 5 = 11  4 × 5 = 16  5 × 5 = 1┬  6 × 5 = 22  7 × 5 = 27  8 × 5 = 2┤  9 × 5 = 33  ┴ × 5 = 38  ┬ × 5 = 3├  ┤ × 5 = 44  ├ × 5 = 49
1 × 6 =  6  2 × 6 =  ┤  3 × 6 = 14  4 × 6 = 1┴  5 × 6 = 22  6 × 6 = 28  7 × 6 = 30  8 × 6 = 36  9 × 6 = 3┤  ┴ × 6 = 44  ┬ × 6 = 4┴  ┤ × 6 = 52  ├ × 6 = 58
1 × 7 =  7  2 × 7 = 10  3 × 7 = 17  4 × 7 = 20  5 × 7 = 27  6 × 7 = 30  7 × 7 = 37  8 × 7 = 40  9 × 7 = 47  ┴ × 7 = 50  ┬ × 7 = 57  ┤ × 7 = 60  ├ × 7 = 67
1 × 8 =  8  2 × 8 = 12  3 × 8 = 1┴  4 × 8 = 24  5 × 8 = 2┤  6 × 8 = 36  7 × 8 = 40  8 × 8 = 48  9 × 8 = 52  ┴ × 8 = 5┴  ┬ × 8 = 64  ┤ × 8 = 6┤  ├ × 8 = 76
1 × 9 =  9  2 × 9 = 14  3 × 9 = 1├  4 × 9 = 28  5 × 9 = 33  6 × 9 = 3┤  7 × 9 = 47  8 × 9 = 52  9 × 9 = 5┬  ┴ × 9 = 66  ┬ × 9 = 71  ┤ × 9 = 7┴  ├ × 9 = 85
1 × ┴ =  ┴  2 × ┴ = 16  3 × ┴ = 22  4 × ┴ = 2┤  5 × ┴ = 38  6 × ┴ = 44  7 × ┴ = 50  8 × ┴ = 5┴  9 × ┴ = 66  ┴ × ┴ = 72  ┬ × ┴ = 7┤  ┤ × ┴ = 88  ├ × ┴ = 94
1 × ┬ =  ┬  2 × ┬ = 18  3 × ┬ = 25  4 × ┬ = 32  5 × ┬ = 3├  6 × ┬ = 4┴  7 × ┬ = 57  8 × ┬ = 64  9 × ┬ = 71  ┴ × ┬ = 7┤  ┬ × ┬ = 89  ┤ × ┬ = 96  ├ × ┬ = ┴3
1 × ┤ =  ┤  2 × ┤ = 1┴  3 × ┤ = 28  4 × ┤ = 36  5 × ┤ = 44  6 × ┤ = 52  7 × ┤ = 60  8 × ┤ = 6┤  9 × ┤ = 7┴  ┴ × ┤ = 88  ┬ × ┤ = 96  ┤ × ┤ = ┴4  ├ × ┤ = ┬2
1 × ├ =  ├  2 × ├ = 1┤  3 × ├ = 2┬  4 × ├ = 3┴  5 × ├ = 49  6 × ├ = 58  7 × ├ = 67  8 × ├ = 76  9 × ├ = 85  ┴ × ├ = 94  ┬ × ├ = ┴3  ┤ × ├ = ┬2  ├ × ├ = ┤1

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7  8 × 1 =  8  9 × 1 =  9  ┴ × 1 =  ┴  ┬ × 1 =  ┬  ┤ × 1 =  ┤  ├ × 1 =  ├  ┌ × 1 =  ┌
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 =  8  5 × 2 =  ┴  6 × 2 =  ┤  7 × 2 =  ┌  8 × 2 = 11  9 × 2 = 13  ┴ × 2 = 15  ┬ × 2 = 17  ┤ × 2 = 19  ├ × 2 = 1┬  ┌ × 2 = 1├
1 × 3 =  3  2 × 3 =  6  3 × 3 =  9  4 × 3 =  ┤  5 × 3 = 10  6 × 3 = 13  7 × 3 = 16  8 × 3 = 19  9 × 3 = 1┤  ┴ × 3 = 20  ┬ × 3 = 23  ┤ × 3 = 26  ├ × 3 = 29  ┌ × 3 = 2┤
1 × 4 =  4  2 × 4 =  8  3 × 4 =  ┤  4 × 4 = 11  5 × 4 = 15  6 × 4 = 19  7 × 4 = 1├  8 × 4 = 22  9 × 4 = 26  ┴ × 4 = 2┴  ┬ × 4 = 2┌  ┤ × 4 = 33  ├ × 4 = 37  ┌ × 4 = 3┬
1 × 5 =  5  2 × 5 =  ┴  3 × 5 = 10  4 × 5 = 15  5 × 5 = 1┴  6 × 5 = 20  7 × 5 = 25  8 × 5 = 2┴  9 × 5 = 30  ┴ × 5 = 35  ┬ × 5 = 3┴  ┤ × 5 = 40  ├ × 5 = 45  ┌ × 5 = 4┴
1 × 6 =  6  2 × 6 =  ┤  3 × 6 = 13  4 × 6 = 19  5 × 6 = 20  6 × 6 = 26  7 × 6 = 2┤  8 × 6 = 33  9 × 6 = 39  ┴ × 6 = 40  ┬ × 6 = 46  ┤ × 6 = 4┤  ├ × 6 = 53  ┌ × 6 = 59
1 × 7 =  7  2 × 7 =  ┌  3 × 7 = 16  4 × 7 = 1├  5 × 7 = 25  6 × 7 = 2┤  7 × 7 = 34  8 × 7 = 3┬  9 × 7 = 43  ┴ × 7 = 4┴  ┬ × 7 = 52  ┤ × 7 = 59  ├ × 7 = 61  ┌ × 7 = 68
1 × 8 =  8  2 × 8 = 11  3 × 8 = 19  4 × 8 = 22  5 × 8 = 2┴  6 × 8 = 33  7 × 8 = 3┬  8 × 8 = 44  9 × 8 = 4┤  ┴ × 8 = 55  ┬ × 8 = 5├  ┤ × 8 = 66  ├ × 8 = 6┌  ┌ × 8 = 77
1 × 9 =  9  2 × 9 = 13  3 × 9 = 1┤  4 × 9 = 26  5 × 9 = 30  6 × 9 = 39  7 × 9 = 43  8 × 9 = 4┤  9 × 9 = 56  ┴ × 9 = 60  ┬ × 9 = 69  ┤ × 9 = 73  ├ × 9 = 7┤  ┌ × 9 = 86
1 × ┴ =  ┴  2 × ┴ = 15  3 × ┴ = 20  4 × ┴ = 2┴  5 × ┴ = 35  6 × ┴ = 40  7 × ┴ = 4┴  8 × ┴ = 55  9 × ┴ = 60  ┴ × ┴ = 6┴  ┬ × ┴ = 75  ┤ × ┴ = 80  ├ × ┴ = 8┴  ┌ × ┴ = 95
1 × ┬ =  ┬  2 × ┬ = 17  3 × ┬ = 23  4 × ┬ = 2┌  5 × ┬ = 3┴  6 × ┬ = 46  7 × ┬ = 52  8 × ┬ = 5├  9 × ┬ = 69  ┴ × ┬ = 75  ┬ × ┬ = 81  ┤ × ┬ = 8┤  ├ × ┬ = 98  ┌ × ┬ = ┴4
1 × ┤ =  ┤  2 × ┤ = 19  3 × ┤ = 26  4 × ┤ = 33  5 × ┤ = 40  6 × ┤ = 4┤  7 × ┤ = 59  8 × ┤ = 66  9 × ┤ = 73  ┴ × ┤ = 80  ┬ × ┤ = 8┤  ┤ × ┤ = 99  ├ × ┤ = ┴6  ┌ × ┤ = ┬3
1 × ├ =  ├  2 × ├ = 1┬  3 × ├ = 29  4 × ├ = 37  5 × ├ = 45  6 × ├ = 53  7 × ├ = 61  8 × ├ = 6┌  9 × ├ = 7┤  ┴ × ├ = 8┴  ┬ × ├ = 98  ┤ × ├ = ┴6  ├ × ├ = ┬4  ┌ × ├ = ┤2
1 × ┌ =  ┌  2 × ┌ = 1├  3 × ┌ = 2┤  4 × ┌ = 3┬  5 × ┌ = 4┴  6 × ┌ = 59  7 × ┌ = 68  8 × ┌ = 77  9 × ┌ = 86  ┴ × ┌ = 95  ┬ × ┌ = ┴4  ┤ × ┌ = ┬3  ├ × ┌ = ┤2  ┌ × ┌ = ├1

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7  8 × 1 =  8  9 × 1 =  9  ┴ × 1 =  ┴  ┬ × 1 =  ┬  ┤ × 1 =  ┤  ├ × 1 =  ├  ┌ × 1 =  ┌  ┐ × 1 =  ┐
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 =  8  5 × 2 =  ┴  6 × 2 =  ┤  7 × 2 =  ┌  8 × 2 = 10  9 × 2 = 12  ┴ × 2 = 14  ┬ × 2 = 16  ┤ × 2 = 18  ├ × 2 = 1┴  ┌ × 2 = 1┤  ┐ × 2 = 1┌
1 × 3 =  3  2 × 3 =  6  3 × 3 =  9  4 × 3 =  ┤  5 × 3 =  ┐  6 × 3 = 12  7 × 3 = 15  8 × 3 = 18  9 × 3 = 1┬  ┴ × 3 = 1┌  ┬ × 3 = 21  ┤ × 3 = 24  ├ × 3 = 27  ┌ × 3 = 2┴  ┐ × 3 = 2├
1 × 4 =  4  2 × 4 =  8  3 × 4 =  ┤  4 × 4 = 10  5 × 4 = 14  6 × 4 = 18  7 × 4 = 1┤  8 × 4 = 20  9 × 4 = 24  ┴ × 4 = 28  ┬ × 4 = 2┤  ┤ × 4 = 30  ├ × 4 = 34  ┌ × 4 = 38  ┐ × 4 = 3┤
1 × 5 =  5  2 × 5 =  ┴  3 × 5 =  ┐  4 × 5 = 14  5 × 5 = 19  6 × 5 = 1┌  7 × 5 = 23  8 × 5 = 28  9 × 5 = 2├  ┴ × 5 = 32  ┬ × 5 = 37  ┤ × 5 = 3┤  ├ × 5 = 41  ┌ × 5 = 46  ┐ × 5 = 4┬
1 × 6 =  6  2 × 6 =  ┤  3 × 6 = 12  4 × 6 = 18  5 × 6 = 1┌  6 × 6 = 24  7 × 6 = 2┴  8 × 6 = 30  9 × 6 = 36  ┴ × 6 = 3┤  ┬ × 6 = 42  ┤ × 6 = 48  ├ × 6 = 4┌  ┌ × 6 = 54  ┐ × 6 = 5┴
1 × 7 =  7  2 × 7 =  ┌  3 × 7 = 15  4 × 7 = 1┤  5 × 7 = 23  6 × 7 = 2┴  7 × 7 = 31  8 × 7 = 38  9 × 7 = 3┐  ┴ × 7 = 46  ┬ × 7 = 4├  ┤ × 7 = 54  ├ × 7 = 5┬  ┌ × 7 = 62  ┐ × 7 = 69
1 × 8 =  8  2 × 8 = 10  3 × 8 = 18  4 × 8 = 20  5 × 8 = 28  6 × 8 = 30  7 × 8 = 38  8 × 8 = 40  9 × 8 = 48  ┴ × 8 = 50  ┬ × 8 = 58  ┤ × 8 = 60  ├ × 8 = 68  ┌ × 8 = 70  ┐ × 8 = 78
1 × 9 =  9  2 × 9 = 12  3 × 9 = 1┬  4 × 9 = 24  5 × 9 = 2├  6 × 9 = 36  7 × 9 = 3┐  8 × 9 = 48  9 × 9 = 51  ┴ × 9 = 5┴  ┬ × 9 = 63  ┤ × 9 = 6┤  ├ × 9 = 75  ┌ × 9 = 7┌  ┐ × 9 = 87
1 × ┴ =  ┴  2 × ┴ = 14  3 × ┴ = 1┌  4 × ┴ = 28  5 × ┴ = 32  6 × ┴ = 3┤  7 × ┴ = 46  8 × ┴ = 50  9 × ┴ = 5┴  ┴ × ┴ = 64  ┬ × ┴ = 6┌  ┤ × ┴ = 78  ├ × ┴ = 82  ┌ × ┴ = 8┤  ┐ × ┴ = 96
1 × ┬ =  ┬  2 × ┬ = 16  3 × ┬ = 21  4 × ┬ = 2┤  5 × ┬ = 37  6 × ┬ = 42  7 × ┬ = 4├  8 × ┬ = 58  9 × ┬ = 63  ┴ × ┬ = 6┌  ┬ × ┬ = 79  ┤ × ┬ = 84  ├ × ┬ = 8┐  ┌ × ┬ = 9┴  ┐ × ┬ = ┴5
1 × ┤ =  ┤  2 × ┤ = 18  3 × ┤ = 24  4 × ┤ = 30  5 × ┤ = 3┤  6 × ┤ = 48  7 × ┤ = 54  8 × ┤ = 60  9 × ┤ = 6┤  ┴ × ┤ = 78  ┬ × ┤ = 84  ┤ × ┤ = 90  ├ × ┤ = 9┤  ┌ × ┤ = ┴8  ┐ × ┤ = ┬4
1 × ├ =  ├  2 × ├ = 1┴  3 × ├ = 27  4 × ├ = 34  5 × ├ = 41  6 × ├ = 4┌  7 × ├ = 5┬  8 × ├ = 68  9 × ├ = 75  ┴ × ├ = 82  ┬ × ├ = 8┐  ┤ × ├ = 9┤  ├ × ├ = ┴9  ┌ × ├ = ┬6  ┐ × ├ = ┤3
1 × ┌ =  ┌  2 × ┌ = 1┤  3 × ┌ = 2┴  4 × ┌ = 38  5 × ┌ = 46  6 × ┌ = 54  7 × ┌ = 62  8 × ┌ = 70  9 × ┌ = 7┌  ┴ × ┌ = 8┤  ┬ × ┌ = 9┴  ┤ × ┌ = ┴8  ├ × ┌ = ┬6  ┌ × ┌ = ┤4  ┐ × ┌ = ├2
1 × ┐ =  ┐  2 × ┐ = 1┌  3 × ┐ = 2├  4 × ┐ = 3┤  5 × ┐ = 4┬  6 × ┐ = 5┴  7 × ┐ = 69  8 × ┐ = 78  9 × ┐ = 87  ┴ × ┐ = 96  ┬ × ┐ = ┴5  ┤ × ┐ = ┬4  ├ × ┐ = ┤3  ┌ × ┐ = ├2  ┐ × ┐ = ┌1

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7  8 × 1 =  8  9 × 1 =  9  ┴ × 1 =  ┴  ┬ × 1 =  ┬  ┤ × 1 =  ┤  ├ × 1 =  ├  ┌ × 1 =  ┌  ┐ × 1 =  ┐  └ × 1 =  └
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 =  8  5 × 2 =  ┴  6 × 2 =  ┤  7 × 2 =  ┌  8 × 2 =  └  9 × 2 = 11  ┴ × 2 = 13  ┬ × 2 = 15  ┤ × 2 = 17  ├ × 2 = 19  ┌ × 2 = 1┬  ┐ × 2 = 1├  └ × 2 = 1┐
1 × 3 =  3  2 × 3 =  6  3 × 3 =  9  4 × 3 =  ┤  5 × 3 =  ┐  6 × 3 = 11  7 × 3 = 14  8 × 3 = 17  9 × 3 = 1┴  ┴ × 3 = 1├  ┬ × 3 = 1└  ┤ × 3 = 22  ├ × 3 = 25  ┌ × 3 = 28  ┐ × 3 = 2┬  └ × 3 = 2┌
1 × 4 =  4  2 × 4 =  8  3 × 4 =  ┤  4 × 4 =  └  5 × 4 = 13  6 × 4 = 17  7 × 4 = 1┬  8 × 4 = 1┐  9 × 4 = 22  ┴ × 4 = 26  ┬ × 4 = 2┴  ┤ × 4 = 2┌  ├ × 4 = 31  ┌ × 4 = 35  ┐ × 4 = 39  └ × 4 = 3├
1 × 5 =  5  2 × 5 =  ┴  3 × 5 =  ┐  4 × 5 = 13  5 × 5 = 18  6 × 5 = 1├  7 × 5 = 21  8 × 5 = 26  9 × 5 = 2┬  ┴ × 5 = 2└  ┬ × 5 = 34  ┤ × 5 = 39  ├ × 5 = 3┌  ┌ × 5 = 42  ┐ × 5 = 47  └ × 5 = 4┤
1 × 6 =  6  2 × 6 =  ┤  3 × 6 = 11  4 × 6 = 17  5 × 6 = 1├  6 × 6 = 22  7 × 6 = 28  8 × 6 = 2┌  9 × 6 = 33  ┴ × 6 = 39  ┬ × 6 = 3┐  ┤ × 6 = 44  ├ × 6 = 4┴  ┌ × 6 = 4└  ┐ × 6 = 55  └ × 6 = 5┬
1 × 7 =  7  2 × 7 =  ┌  3 × 7 = 14  4 × 7 = 1┬  5 × 7 = 21  6 × 7 = 28  7 × 7 = 2┐  8 × 7 = 35  9 × 7 = 3┤  ┴ × 7 = 42  ┬ × 7 = 49  ┤ × 7 = 4└  ├ × 7 = 56  ┌ × 7 = 5├  ┐ × 7 = 63  └ × 7 = 6┴
1 × 8 =  8  2 × 8 =  └  3 × 8 = 17  4 × 8 = 1┐  5 × 8 = 26  6 × 8 = 2┌  7 × 8 = 35  8 × 8 = 3├  9 × 8 = 44  ┴ × 8 = 4┤  ┬ × 8 = 53  ┤ × 8 = 5┬  ├ × 8 = 62  ┌ × 8 = 6┴  ┐ × 8 = 71  └ × 8 = 79
1 × 9 =  9  2 × 9 = 11  3 × 9 = 1┴  4 × 9 = 22  5 × 9 = 2┬  6 × 9 = 33  7 × 9 = 3┤  8 × 9 = 44  9 × 9 = 4├  ┴ × 9 = 55  ┬ × 9 = 5┌  ┤ × 9 = 66  ├ × 9 = 6┐  ┌ × 9 = 77  ┐ × 9 = 7└  └ × 9 = 88
1 × ┴ =  ┴  2 × ┴ = 13  3 × ┴ = 1├  4 × ┴ = 26  5 × ┴ = 2└  6 × ┴ = 39  7 × ┴ = 42  8 × ┴ = 4┤  9 × ┴ = 55  ┴ × ┴ = 5┐  ┬ × ┴ = 68  ┤ × ┴ = 71  ├ × ┴ = 7┬  ┌ × ┴ = 84  ┐ × ┴ = 8┌  └ × ┴ = 97
1 × ┬ =  ┬  2 × ┬ = 15  3 × ┬ = 1└  4 × ┬ = 2┴  5 × ┬ = 34  6 × ┬ = 3┐  7 × ┬ = 49  8 × ┬ = 53  9 × ┬ = 5┌  ┴ × ┬ = 68  ┬ × ┬ = 72  ┤ × ┬ = 7├  ├ × ┬ = 87  ┌ × ┬ = 91  ┐ × ┬ = 9┤  └ × ┬ = ┴6
1 × ┤ =  ┤  2 × ┤ = 17  3 × ┤ = 22  4 × ┤ = 2┌  5 × ┤ = 39  6 × ┤ = 44  7 × ┤ = 4└  8 × ┤ = 5┬  9 × ┤ = 66  ┴ × ┤ = 71  ┬ × ┤ = 7├  ┤ × ┤ = 88  ├ × ┤ = 93  ┌ × ┤ = 9┐  ┐ × ┤ = ┴┴  └ × ┤ = ┬5
1 × ├ =  ├  2 × ├ = 19  3 × ├ = 25  4 × ├ = 31  5 × ├ = 3┌  6 × ├ = 4┴  7 × ├ = 56  8 × ├ = 62  9 × ├ = 6┐  ┴ × ├ = 7┬  ┬ × ├ = 87  ┤ × ├ = 93  ├ × ├ = 9└  ┌ × ├ = ┴┤  ┐ × ├ = ┬8  └ × ├ = ┤4
1 × ┌ =  ┌  2 × ┌ = 1┬  3 × ┌ = 28  4 × ┌ = 35  5 × ┌ = 42  6 × ┌ = 4└  7 × ┌ = 5├  8 × ┌ = 6┴  9 × ┌ = 77  ┴ × ┌ = 84  ┬ × ┌ = 91  ┤ × ┌ = 9┐  ├ × ┌ = ┴┤  ┌ × ┌ = ┬9  ┐ × ┌ = ┤6  └ × ┌ = ├3
1 × ┐ =  ┐  2 × ┐ = 1├  3 × ┐ = 2┬  4 × ┐ = 39  5 × ┐ = 47  6 × ┐ = 55  7 × ┐ = 63  8 × ┐ = 71  9 × ┐ = 7└  ┴ × ┐ = 8┌  ┬ × ┐ = 9┤  ┤ × ┐ = ┴┴  ├ × ┐ = ┬8  ┌ × ┐ = ┤6  ┐ × ┐ = ├4  └ × ┐ = ┌2
1 × └ =  └  2 × └ = 1┐  3 × └ = 2┌  4 × └ = 3├  5 × └ = 4┤  6 × └ = 5┬  7 × └ = 6┴  8 × └ = 79  9 × └ = 88  ┴ × └ = 97  ┬ × └ = ┴6  ┤ × └ = ┬5  ├ × └ = ┤4  ┌ × └ = ├3  ┐ × └ = ┌2  └ × └ = ┐1

1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7  8 × 1 =  8  9 × 1 =  9  ┴ × 1 =  ┴  ┬ × 1 =  ┬  ┤ × 1 =  ┤  ├ × 1 =  ├  ┌ × 1 =  ┌  ┐ × 1 =  ┐  └ × 1 =  └  ┘ × 1 =  ┘
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 =  8  5 × 2 =  ┴  6 × 2 =  ┤  7 × 2 =  ┌  8 × 2 =  └  9 × 2 = 10  ┴ × 2 = 12  ┬ × 2 = 14  ┤ × 2 = 16  ├ × 2 = 18  ┌ × 2 = 1┴  ┐ × 2 = 1┤  └ × 2 = 1┌  ┘ × 2 = 1└
1 × 3 =  3  2 × 3 =  6  3 × 3 =  9  4 × 3 =  ┤  5 × 3 =  ┐  6 × 3 = 10  7 × 3 = 13  8 × 3 = 16  9 × 3 = 19  ┴ × 3 = 1┤  ┬ × 3 = 1┐  ┤ × 3 = 20  ├ × 3 = 23  ┌ × 3 = 26  ┐ × 3 = 29  └ × 3 = 2┤  ┘ × 3 = 2┐
1 × 4 =  4  2 × 4 =  8  3 × 4 =  ┤  4 × 4 =  └  5 × 4 = 12  6 × 4 = 16  7 × 4 = 1┴  8 × 4 = 1┌  9 × 4 = 20  ┴ × 4 = 24  ┬ × 4 = 28  ┤ × 4 = 2┤  ├ × 4 = 2└  ┌ × 4 = 32  ┐ × 4 = 36  └ × 4 = 3┴  ┘ × 4 = 3┌
1 × 5 =  5  2 × 5 =  ┴  3 × 5 =  ┐  4 × 5 = 12  5 × 5 = 17  6 × 5 = 1┤  7 × 5 = 1┘  8 × 5 = 24  9 × 5 = 29  ┴ × 5 = 2┌  ┬ × 5 = 31  ┤ × 5 = 36  ├ × 5 = 3┬  ┌ × 5 = 3└  ┐ × 5 = 43  └ × 5 = 48  ┘ × 5 = 4├
1 × 6 =  6  2 × 6 =  ┤  3 × 6 = 10  4 × 6 = 16  5 × 6 = 1┤  6 × 6 = 20  7 × 6 = 26  8 × 6 = 2┤  9 × 6 = 30  ┴ × 6 = 36  ┬ × 6 = 3┤  ┤ × 6 = 40  ├ × 6 = 46  ┌ × 6 = 4┤  ┐ × 6 = 50  └ × 6 = 56  ┘ × 6 = 5┤
1 × 7 =  7  2 × 7 =  ┌  3 × 7 = 13  4 × 7 = 1┴  5 × 7 = 1┘  6 × 7 = 26  7 × 7 = 2├  8 × 7 = 32  9 × 7 = 39  ┴ × 7 = 3└  ┬ × 7 = 45  ┤ × 7 = 4┤  ├ × 7 = 51  ┌ × 7 = 58  ┐ × 7 = 5┐  └ × 7 = 64  ┘ × 7 = 6┬
1 × 8 =  8  2 × 8 =  └  3 × 8 = 16  4 × 8 = 1┌  5 × 8 = 24  6 × 8 = 2┤  7 × 8 = 32  8 × 8 = 3┴  9 × 8 = 40  ┴ × 8 = 48  ┬ × 8 = 4└  ┤ × 8 = 56  ├ × 8 = 5┌  ┌ × 8 = 64  ┐ × 8 = 6┤  └ × 8 = 72  ┘ × 8 = 7┴
1 × 9 =  9  2 × 9 = 10  3 × 9 = 19  4 × 9 = 20  5 × 9 = 29  6 × 9 = 30  7 × 9 = 39  8 × 9 = 40  9 × 9 = 49  ┴ × 9 = 50  ┬ × 9 = 59  ┤ × 9 = 60  ├ × 9 = 69  ┌ × 9 = 70  ┐ × 9 = 79  └ × 9 = 80  ┘ × 9 = 89
1 × ┴ =  ┴  2 × ┴ = 12  3 × ┴ = 1┤  4 × ┴ = 24  5 × ┴ = 2┌  6 × ┴ = 36  7 × ┴ = 3└  8 × ┴ = 48  9 × ┴ = 50  ┴ × ┴ = 5┴  ┬ × ┴ = 62  ┤ × ┴ = 6┤  ├ × ┴ = 74  ┌ × ┴ = 7┌  ┐ × ┴ = 86  └ × ┴ = 8└  ┘ × ┴ = 98
1 × ┬ =  ┬  2 × ┬ = 14  3 × ┬ = 1┐  4 × ┬ = 28  5 × ┬ = 31  6 × ┬ = 3┤  7 × ┬ = 45  8 × ┬ = 4└  9 × ┬ = 59  ┴ × ┬ = 62  ┬ × ┬ = 6├  ┤ × ┬ = 76  ├ × ┬ = 7┘  ┌ × ┬ = 8┴  ┐ × ┬ = 93  └ × ┬ = 9┌  ┘ × ┬ = ┴7
1 × ┤ =  ┤  2 × ┤ = 16  3 × ┤ = 20  4 × ┤ = 2┤  5 × ┤ = 36  6 × ┤ = 40  7 × ┤ = 4┤  8 × ┤ = 56  9 × ┤ = 60  ┴ × ┤ = 6┤  ┬ × ┤ = 76  ┤ × ┤ = 80  ├ × ┤ = 8┤  ┌ × ┤ = 96  ┐ × ┤ = ┴0  └ × ┤ = ┴┤  ┘ × ┤ = ┬6
1 × ├ =  ├  2 × ├ = 18  3 × ├ = 23  4 × ├ = 2└  5 × ├ = 3┬  6 × ├ = 46  7 × ├ = 51  8 × ├ = 5┌  9 × ├ = 69  ┴ × ├ = 74  ┬ × ├ = 7┘  ┤ × ├ = 8┤  ├ × ├ = 97  ┌ × ├ = ┴2  ┐ × ├ = ┴┐  └ × ├ = ┬┴  ┘ × ├ = ┤5
1 × ┌ =  ┌  2 × ┌ = 1┴  3 × ┌ = 26  4 × ┌ = 32  5 × ┌ = 3└  6 × ┌ = 4┤  7 × ┌ = 58  8 × ┌ = 64  9 × ┌ = 70  ┴ × ┌ = 7┌  ┬ × ┌ = 8┴  ┤ × ┌ = 96  ├ × ┌ = ┴2  ┌ × ┌ = ┴└  ┐ × ┌ = ┬┤  └ × ┌ = ┤8  ┘ × ┌ = ├4
1 × ┐ =  ┐  2 × ┐ = 1┤  3 × ┐ = 29  4 × ┐ = 36  5 × ┐ = 43  6 × ┐ = 50  7 × ┐ = 5┐  8 × ┐ = 6┤  9 × ┐ = 79  ┴ × ┐ = 86  ┬ × ┐ = 93  ┤ × ┐ = ┴0  ├ × ┐ = ┴┐  ┌ × ┐ = ┬┤  ┐ × ┐ = ┤9  └ × ┐ = ├6  ┘ × ┐ = ┌3
1 × └ =  └  2 × └ = 1┌  3 × └ = 2┤  4 × └ = 3┴  5 × └ = 48  6 × └ = 56  7 × └ = 64  8 × └ = 72  9 × └ = 80  ┴ × └ = 8└  ┬ × └ = 9┌  ┤ × └ = ┴┤  ├ × └ = ┬┴  ┌ × └ = ┤8  ┐ × └ = ├6  └ × └ = ┌4  ┘ × └ = ┐2
1 × ┘ =  ┘  2 × ┘ = 1└  3 × ┘ = 2┐  4 × ┘ = 3┌  5 × ┘ = 4├  6 × ┘ = 5┤  7 × ┘ = 6┬  8 × ┘ = 7┴  9 × ┘ = 89  ┴ × ┘ = 98  ┬ × ┘ = ┴7  ┤ × ┘ = ┬6  ├ × ┘ = ┤5  ┌ × ┘ = ├4  ┐ × ┘ = ┌3  └ × ┘ = ┐2  ┘ × ┘ = └1
```

我們可以發現乘法表有個特性，就以十進位的來舉例，首先他們的個位數是左右對稱的，由下圖可看見，A和I列分別是123456789和987654321，而B和H列分別是246802468和864208642，也就是顛倒過來看相同，其他列也是相同道理，分別是CG:369258147、DF:482604826和E:505050505，而這個乘法表又有一個特殊的特點，如果X進位的X除以二能整除得到N(X是十進位)，那麼用那個進位所表示的數字，個位數如果是N或是0即是代表那個數字是N的倍數，以10進位來說，10÷2=5，則數字25、30因為尾數是0或5所以是5的倍數，而以6進位來說，6÷2=3，則數字23、50因為尾數是0、3所以是3的倍數。
```
         A           B           C           D           E           F           G           H           I
1 × 1 =  1  2 × 1 =  2  3 × 1 =  3  4 × 1 =  4  5 × 1 =  5  6 × 1 =  6  7 × 1 =  7  8 × 1 =  8  9 × 1 =  9
1 × 2 =  2  2 × 2 =  4  3 × 2 =  6  4 × 2 =  8  5 × 2 = 10  6 × 2 = 12  7 × 2 = 14  8 × 2 = 16  9 × 2 = 18
1 × 3 =  3  2 × 3 =  6  3 × 3 =  9  4 × 3 = 12  5 × 3 = 15  6 × 3 = 18  7 × 3 = 21  8 × 3 = 24  9 × 3 = 27
1 × 4 =  4  2 × 4 =  8  3 × 4 = 12  4 × 4 = 16  5 × 4 = 20  6 × 4 = 24  7 × 4 = 28  8 × 4 = 32  9 × 4 = 36
1 × 5 =  5  2 × 5 = 10  3 × 5 = 15  4 × 5 = 20  5 × 5 = 25  6 × 5 = 30  7 × 5 = 35  8 × 5 = 40  9 × 5 = 45
1 × 6 =  6  2 × 6 = 12  3 × 6 = 18  4 × 6 = 24  5 × 6 = 30  6 × 6 = 36  7 × 6 = 42  8 × 6 = 48  9 × 6 = 54
1 × 7 =  7  2 × 7 = 14  3 × 7 = 21  4 × 7 = 28  5 × 7 = 35  6 × 7 = 42  7 × 7 = 49  8 × 7 = 56  9 × 7 = 63
1 × 8 =  8  2 × 8 = 16  3 × 8 = 24  4 × 8 = 32  5 × 8 = 40  6 × 8 = 48  7 × 8 = 56  8 × 8 = 64  9 × 8 = 72
1 × 9 =  9  2 × 9 = 18  3 × 9 = 27  4 × 9 = 36  5 × 9 = 45  6 × 9 = 54  7 × 9 = 63  8 × 9 = 72  9 × 9 = 81
```

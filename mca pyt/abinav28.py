{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f7500574",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number:5\n",
      "number is positive\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"enter a number:\"))\n",
    "if n>0:\n",
    "    print(\"number is positive\")\n",
    "else: \n",
    "    print(\"number is negative\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "512bc28e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a number:4\n",
      "number is even\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"enter a number:\"))\n",
    "if n%2==0:\n",
    "    print(\"number is even\")\n",
    "else: \n",
    "    print(\"number is odd\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e38b1c3c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the first number:5\n",
      "enter the second number:12\n",
      "12 is greater\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"enter the first number:\"))\n",
    "n1=int(input(\"enter the second number:\"))\n",
    "if n>n1:\n",
    "    print(f\"{n}  is greater\")\n",
    "else: \n",
    "    print(f\"{n1} is greater\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8974822c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number9\n",
      "not divisible \n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"enter the number\"))\n",
    "if n%5==0:\n",
    "    print(\"divisible\")\n",
    "else: \n",
    "    print(\"not divisible \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "323f712b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the radius of the circle3\n",
      "28.259999999999998\n"
     ]
    }
   ],
   "source": [
    "r=int(input(\"Enter the radius of the circle\"))\n",
    "pi=3.14\n",
    "area=pi*r*r\n",
    "print(area)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "3fee5a31",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the celcius34\n",
      "93.2\n"
     ]
    }
   ],
   "source": [
    "c=float(input(\"Enter the celcius\"))\n",
    "f=c*9/5+32\n",
    "print(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "84a96483",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the fahrenheit100.4\n",
      "38.0\n"
     ]
    }
   ],
   "source": [
    "f=float(input(\"Enter the fahrenheit\"))\n",
    "c=(f-32)*5/9\n",
    "print(c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "c3ba4a96",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number5\n",
      "positive\n"
     ]
    }
   ],
   "source": [
    "num=int(input(\"Enter a number\"))\n",
    "if num>0:\n",
    "     print(\"positive\")\n",
    "elif num<0:\n",
    "        print(\"negative\")\n",
    "else:\n",
    "        print(\"Zero\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "1f485720",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number5\n",
      "odd\n"
     ]
    }
   ],
   "source": [
    "num=int(input(\"Enter a number\"))\n",
    "if num %2 == 0:\n",
    "    print(\"even\")\n",
    "else:\n",
    "    print(\"odd\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "fffa7a27",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number:4\n",
      "Enter second number:8\n",
      "num1 not equal to num2\n"
     ]
    }
   ],
   "source": [
    "num1=int(input(\"Enter a number:\"))\n",
    "num2=int(input(\"Enter second number:\"))\n",
    "if num1 == num2:\n",
    "    print(\"num1 equal to num2\")\n",
    "else:\n",
    "    print(\"num1 not equal to num2\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "799bf05a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number100\n",
      "Entered num is 100\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"Enter a number\"))\n",
    "if n>100:\n",
    "    print(\"Number is greater than 100\")\n",
    "elif n<100:\n",
    "            print(\"Number is lesser than 100\")\n",
    "else:\n",
    "            print(\"Entered num is 100\")\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "50343b87",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter first number5\n",
      "Enter second number7\n",
      "Biggest = 7\n"
     ]
    }
   ],
   "source": [
    "a = int(input(\"enter first number\"))\n",
    "b = int(input(\"Enter second number\"))\n",
    "if a>b:\n",
    "    print(\"Biggest =\",a)\n",
    "else:\n",
    "    print(\"Biggest =\",b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "12eae771",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your age17\n",
      "Not eligible to vote\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"Enter your age\"))\n",
    "if age>=18:\n",
    "    print(\"Eligible to vote\")\n",
    "else:\n",
    "    print(\"Not eligible to vote\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "da8cc034",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the mark79\n",
      "B grade\n"
     ]
    }
   ],
   "source": [
    "mark =int(input(\"Enter the mark\"))\n",
    "if mark>=90:\n",
    "    print(\"A grade\")\n",
    "elif mark>=75:\n",
    "        print(\"B grade\")\n",
    "elif mark>=75:\n",
    "        print(\"C grade\")\n",
    "else:\n",
    "        print(\"Failed\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "0c11c7b7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the first number:6\n",
      "Enter the second number:8\n",
      "Enter the third number:12\n",
      "c is the greatest\n"
     ]
    }
   ],
   "source": [
    "a=int(input(\"Enter the first number:\"))\n",
    "b=int(input(\"Enter the second number:\"))\n",
    "c=int(input(\"Enter the third number:\"))\n",
    "if a > b and b > c:\n",
    "      print(\"a is the greatest\")\n",
    "elif b > c and c > a:\n",
    "      print(\"b is the greatest\")\n",
    "else:\n",
    "      print(\"c is the greatest\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "60ea43ee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter your age:17\n",
      "you are a teenager\n"
     ]
    }
   ],
   "source": [
    "age = int(input(\"Enter your age:\"))\n",
    "if age < 13:\n",
    "    print(\"you are a child\")\n",
    "elif age <18:\n",
    "        print(\"you are a teenager\")\n",
    "else:\n",
    "        print(\"you are a adult\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "615142c1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the Day number8\n",
      "invalid\n"
     ]
    }
   ],
   "source": [
    "int(input(\"Enter the Day number\"))\n",
    "if n==1:\n",
    "       print(\"monday\")\n",
    "elif n==2:\n",
    "        print(\"tuesday\")\n",
    "elif n==3:\n",
    "        print(\"wednesday\")\n",
    "elif n==4:\n",
    "        print(\"thursday\")\n",
    "elif n==5:\n",
    "        print(\"friday\")\n",
    "elif n==6:\n",
    "        print(\"saturday\")\n",
    "elif n==7:\n",
    "        print(\"sunday\")\n",
    "else:\n",
    "        print(\"invalid\")\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "da3c3c45",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number24\n",
      "not divisible \n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"enter the number\"))\n",
    "if n%7==0:\n",
    "    print(\"divisible\")\n",
    "else: \n",
    "    print(\"not divisible \")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f8a9b48a",
   "metadata": {},
   "outputs": [],
   "source": [
    "ch=input(\"Enter the character\")\n",
    "if ch in \"aeiouAEIOU\":\n",
    "    print(\"Vowel\")\n",
    "else:\n",
    "    print(\"Not vowel\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "20dd9802",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the age21\n",
      "Eligible to apply\n"
     ]
    }
   ],
   "source": [
    "age=int(input(\"enter the age\"))\n",
    "if age>=18:\n",
    "    print(\"Eligible to apply\")\n",
    "else:\n",
    "    print(\"Not eligible\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8a1f63de",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the first stringget\n",
      "enter the second stringget\n",
      "strings are equal\n"
     ]
    }
   ],
   "source": [
    "str1=(input(\"enter the first string\"))\n",
    "str2=(input(\"enter the second string\"))\n",
    "if str1==str2:\n",
    "    print(\"strings are equal\")\n",
    "else:\n",
    "        print(\"strings are not equal\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "77fc39d4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter purchase amount6000\n",
      "Eligible for discount\n"
     ]
    }
   ],
   "source": [
    "amount=float(input(\"Enter purchase amount\"))\n",
    "if amount>5000:\n",
    "    print(\"Eligible for discount\")\n",
    "else:\n",
    "    print(\"Not eligible for discount\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3985b22c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number:102\n",
      "the numer doesn't lies between 10 and 100\n"
     ]
    }
   ],
   "source": [
    "num=int(input(\"enter the number:\"))\n",
    "if num>10 and num<=100:\n",
    "    print(\"the numer lies between 10 and 100\")\n",
    "else:\n",
    "    print(\"the numer doesn't lies between 10 and 100\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "09ff2357",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the attendance:84\n",
      "Eligible\n"
     ]
    }
   ],
   "source": [
    "attendance=int(input(\"Enter the attendance:\"))\n",
    "if attendance>=75:\n",
    "    print(\"Eligible\")\n",
    "else:\n",
    "    print(\"Not eligible\")\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "53e7054b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the alphabetA\n",
      "alphabet is in uppercase\n"
     ]
    }
   ],
   "source": [
    "ch=(input(\"Enter the alphabet\"))\n",
    "if ch.isupper():\n",
    "    print(\"alphabet is in uppercase\")\n",
    "else:\n",
    "    print(\"alphabet is in lower case\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "6440ecf7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter the number :455\n",
      "three digit number\n"
     ]
    }
   ],
   "source": [
    "num=int(input(\"enter the number :\"))\n",
    "if num>=100 and num<=999:\n",
    "    print(\"three digit number\")\n",
    "else:\n",
    "    pirnt(\"not a three digit number\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "7475fe4a",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the data used in GB :2\n",
      "Moderate usage\n"
     ]
    }
   ],
   "source": [
    "data=int(input(\"Enter the data used in GB :\"))\n",
    "if data<2:\n",
    "    print(\"Low usage\")\n",
    "elif data<=5:\n",
    "    print(\"Moderate usage\")\n",
    "else:\n",
    "    print(\"High usage\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3cdb96d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "2\n",
      "3\n",
      "4\n",
      "5\n",
      "6\n",
      "7\n",
      "8\n",
      "9\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "for i in range(1,11):\n",
    "    print(i)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "38c0f97d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2\n",
      "4\n",
      "6\n",
      "8\n",
      "10\n",
      "12\n",
      "14\n",
      "16\n",
      "18\n",
      "20\n"
     ]
    }
   ],
   "source": [
    "for i in range(2, 22, 2):\n",
    "    print(i)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "296faebb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n",
      "3\n",
      "5\n",
      "7\n",
      "9\n",
      "11\n",
      "13\n",
      "15\n",
      "17\n",
      "19\n"
     ]
    }
   ],
   "source": [
    "for i in range(1, 20, 2):\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "896d883a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the number:6\n",
      "Sum = 1\n",
      "Sum = 2\n",
      "Sum = 3\n",
      "Sum = 4\n",
      "Sum = 5\n",
      "Sum = 6\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"Enter the number:\"))\n",
    "sum=0\n",
    "for i in range(1, n+1):\n",
    "    sum= sum+1\n",
    "    print(\"Sum =\",sum)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "62d778f4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number:8\n",
      "8 x 1 = 8\n",
      "8 x 2 = 16\n",
      "8 x 3 = 24\n",
      "8 x 4 = 32\n",
      "8 x 5 = 40\n",
      "8 x 6 = 48\n",
      "8 x 7 = 56\n",
      "8 x 8 = 64\n",
      "8 x 9 = 72\n",
      "8 x 10 = 80\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"Enter a number:\"))\n",
    "for i in range(1,11):\n",
    "    print(n, \"x\",i ,\"=\",n*i)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a960fff3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number:6\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n",
      "\n"
     ]
    }
   ],
   "source": [
    "n=int(input(\"Enter a number:\"))\n",
    "fact = 1\n",
    "for i in range(1,n+1):\n",
    "    fact = fact*i\n",
    "    print()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "bcec06db",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter a number:5\n",
      "Result= 615\n"
     ]
    }
   ],
   "source": [
    "n= int(input(\"Enter a number:\"))\n",
    "nn=n*11\n",
    "nnn=n*111\n",
    "result=n+nn+nnn\n",
    "print(\"Result=\",result)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "e40ac889",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter the radius of the circle7\n",
      "153.86\n"
     ]
    }
   ],
   "source": [
    "r=int(input(\"Enter the radius of the circle\"))\n",
    "pi=3.14\n",
    "area=pi*r*r\n",
    "print(area)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "1198e365",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "enter a string:orange\n",
      "Newstring= erango\n"
     ]
    }
   ],
   "source": [
    "s=input(\"enter a string:\")\n",
    "new_string = s[-1]+ s[1:-1]+ s[0]\n",
    "print(\"Newstring=\",new_string)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7b298c68",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter two strings:hello world\n",
      "wollo herld\n"
     ]
    }
   ],
   "source": [
    " s1,s2 =input(\"Enter two strings:\").split()\n",
    " new_s1 = s2[:2]   +s1[2:]\n",
    " new_s2 = s1[:2]   +s2[2:]\n",
    " print(new_s1,new_s2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c05814c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

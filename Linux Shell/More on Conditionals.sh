#!\bin\bash
read a
read b
read c

if [ $a == $b ]; then
    if [ $b == $c ]; then
        echo "EQUILATERAL";
    else
        echo "ISOSCELES";
    fi
elif [ $a == $c ]; then
    if [ $b == $c ]; then
        echo "EQUILATERAL";
    else
        echo "ISOSCELES";
    fi
elif [ $b == $c ]; then
    if [ $a == $c ]; then
        echo "EQUILATERAL";
    else
        echo "ISOSCELES";
    fi
else
    echo "SCALENE";
fi

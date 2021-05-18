<?php
// https://qiita.com/chimayu/items/118898f36d60a7a0ee6a
// https://panda-program.com/posts/how-to-set-up-development-environment-of-at-coder-with-php

// // ABC200 A
// $n = trim(fgets(STDIN));
// echo (int)(($n-1)/100 + 1) . PHP_EOL;

// // ABC200 C
// $n = trim(fgets(STDIN));
// $a = explode( ' ', trim(fgets(STDIN)) );
 
// $list = array_fill(0, 200, 0);
 
// for($i=0; $i<$n; $i++){
//   $amari = $a[$i]%200;
//   $list[$amari]++;
//   unset($a[$i]);
// }
 
// $ans = 0;
// for ($i=0; $i < 200; $i++) {
//   # 0 -> 0, 1 -> 0, 2 -> 1, 3 -> 3, 4 -> 6, ...
//   $n_amari_i = $list[$i];
//   unset($list[$i]);
//   if($n_amari_i==0){
//     continue;
//   }
//   $ans += $n_amari_i*($n_amari_i-1) / 2;
// }
 
// printf("%d\n", $ans);

$s = trim(fgets(STDIN));
$maru = 0;
$batu = 0;
$hatena = 0;
for($i=0; $i<10; $i++){
    if($s[$i]=='x'){
        $batu++;
    }
    elseif($s[$i]=='o'){
        $maru++;
    }
    else{
        $hatena++;
    }
}

if ($maru>4){
    printf("%d\n", 0);
}
elseif ($maru==4){
    printf("%d\n", 1);
}
elseif ($maru==3){
    printf("%d\n", ($maru+$hatena)^4-);
}
return


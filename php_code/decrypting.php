<?php
    // find_prim() finder den hemmelige nøgle d, samt primtallene der er
    // brugt. Den bygger på Fermats metode. Funktionen skal bruge de offentlige
    // nøgler.
    function find_prim($n,$e){
        // $k findes sådan at $k2 er det laveste hele tal større end $n.
        $k=round(sqrt($n));
        $i=0;
        // Følgende finder den værdi, hvor $x2−$n giver et kvadrattal. For at
        // teste om det giver et kvadrattal, tages kvadratroden af $yy og afrundes,
        // derefter tages kvadratet af dette. Kvadratet af det afrundet tal, vil
        // kun give $yy, hvis tallet er et kvadrattal.
        do{
            $yy=bcpow($k+$i ,2)-$n;
            $x=$k+$i;
            $i++;
        }while(bcpow(round(sqrt($yy )) ,2)!= $yy);
        
        // $y udregnes, og ud fra $y og $x kan primtallene $q og $p findes. $k
        // eller φ(n) kan også udregnes nu.
        $y=sqrt($yy);
        $p=$x+$y;
        $q=$x -$y;
        $k = ($p -1)*($q -1);
        // Den hemmelige nøgle kan findes, ved brug af funktionen find_d(), da
        // man nu kender både e og k, der skrives $e og $k.
        $d=find_d($e ,$k);

        return array($p ,$q ,$d);
    }
    // Da nøglerne nu kendes kan funktion dekrypter() bruges, til at dekryptere
    // en besked.
?>
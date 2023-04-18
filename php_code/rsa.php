<?php
    // Functionen tjek_primtal() tjekker om et givet tal er et primtal.
    function tjek_primtal($tal){
        if (($tal == 1) or ($tal == 0)) {
            return false;
        // Er tallet 1 eller 0, er det ikke et primtal, derfor sendes false tilbage.
        }
        // Tallet testes for, om det er et primtal, ved at tjekke om nogen tal
        // går op i det givet tal. Der er ikke nogen grund til at teste 1, da 1
        // går op i alle tal, derfor starter $i med at være 2. Derudover er der
        // ikke nogen tal over halvdelen af det givet tal, der vil gå op i det givet
        // tal, der for testes kun $tal/2 og under.
        for ($i = 2; $i <= ($tal / 2); $i++) {
            if($tal % $i == 0) {
                return false;
            // Hvis et tal går op i det givet tal, er det ikke et primtal, og false
            // returneres.
            }
        }
        return true;
        // Er tallet over 1, og ingen andre tal går op i tallet, må det være
        // et primtal. true returneres derfor.
    }

    // primtal() finder alle primtal, mellem $min og $max, og sætter dem i en liste.
    function primtal($min ,$max){
        $tal=$min;
        $prim =[];
        while($tal <=$max){
        // tjek_primtal() bruges til at teste, om det er et primtal, er det tilfældet
        // sættes primtallet i listen $prim.
            if(tjek_primtal($tal )=== true){
                $prim []= $tal;
            }
            $tal ++;
        }
        return $prim;
    }
    // bestem_e() bestemmer e, sådan at (e,$k)=1
    function bestem_e($k,$min){
        // Følgende laver en liste over alle primtal, mindre end det interval
        // der bruges til at bestemme primtallene. 2 springes over, da $k er et
        // lige tal.
        $prim=primtal(3,$min);
        // Nedstående tjekker om ($prim[$i],$k)=1. Er det tilfældet er e fundet,
        // og det returneres.
        while(sfd($prim[$i],$k )!=1){
            $i++;
        }
        return $prim[$i];
    }

    // sfd() finder største fælles divisor
    function sfd($a, $b)
    {
        // Er enten $a eller $b lig med 0, er den modsatte den største
        // fælles divisor. Ifølge (14)
        if ($a == 0){
            return $b;
        }
        if ($b == 0){
            return $a;
        }
        // Er $a og $b ens, er den største fælles divisor både $a og $b.
        if($a == $b){
            return $a ;
        }
        // Finder resten af det største tal, indtil $a eller $b er 0.
        // Metoden følger af (14).
        if($a > $b) {
            return sfd( $a -$b , $b ) ;
        }
            return sfd( $a , $b -$a ) ;
        }
    // find_d() finder d, sådan at ed ≡1 (mod n).
    function find_d($e,$k){
        $q=0;
        do{
            // Da ed ≡ 1 (mod φ(n)) også kan skrives som d = (φ(n) · q + 1)/e. Der
            // ændres på q i stedet for d, da dette vil være hurtigere. Resultatet
            // afrundes, da q sjældent er et helt tal. φ(n) er $k.
            $d=round(($k*$q+1)/$e);
            $q++;
        }
        // Tjekker om ed (mod φ(n)) = 1 er opfyldt. Er det opfyldt er d fundet.
        while(bcmod(bcmod($e,$k)*bcmod($d,$k),$k )!=1);

        return $d;
    }

    // opretnogler() opretter de nøgler, der skal bruges til krypteringen.
    function opretnogler($min ,$max){
        // Først findes primtallene. For at gøre det laves en liste med primtal
        // mellem $min og $max, ved brug af primtal(). Herefter vælges to tilfældige
        // primtal, der ikke er ens.
        $prim=primtal($min ,$max);
        $p=$q=$prim[rand(0,count($prim )-1)];

        while($q==$p){
            $p=$prim[rand(0,count($prim )-1)];
        }
        // n og φ(n) beregnes som $n og $k.
        $n = $p*$q;
        $k = ($p -1)*($q -1);
        // e er $e, og bestemmes ud fra $k, og $min sikrer at $e er mindre end
        // $k.
        $e=bestem_e($k ,$min);
        // Ud fra $e og $k findes $d, som er den hemmelige nøgle.
        $d=find_d($e ,$k);
        // Nøglerne er nu bestemt og sendes tilbage i en liste.
        return array($d , $e , $n);
    }

    // krypter() krypterer den besked, $bes, der skal krypteres.
    function krypter($bes ,$min ,$max){
        // Den oprindelige besked gemmes i variablen $besked.
        $besked = $bes;
        // Længden af beskeden findes, og er længden ulige tilføjes et mellemrum.
        $bes_l = strlen($bes);
        if(1== $bes_l %2){
        $bes.= "␣";
        }
        // Nøglerne oprettes, hvor primtallene bestemmes mellem $min og $max.
        $nogler = opretnogler($min ,$max);
        $d=$nogler [0];
        $e=$nogler [1];
        $n=$nogler [2];
        // Tegn omskrives til tal.
        $tegn = array("a", "b", "c", "d", "e", "f", "g", "h",
        "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
        "t", "u", "v", "w", "x", "y", "å", "A", "B", "C", "D",
        "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "␣", ".", ",", ":", "-", "/");
        $tal = array("01", "02", "03", "04", "05", "06", "07",
        "08", "09", "10", "11", "12", "13", "14", "15", "16",
        "17", "18", "19", "20", "21", "22", "23", "24", "25",
        "26", "27", "28", "29", "30", "31", "32", "33", "34",
        "35", "36", "37", "38", "39", "40", "41", "42", "43",
        "44", "45", "46", "47", "48", "49", "50", "51", "52",
        "53", "54", "55", "56", "57", "58");
        $bes = str_replace($tegn , $tal , $bes);
    // Tallene deles op i blokke af fire cifre.
    $bes = str_split($bes ,4);
    // Hver blok krypteres nu, og adskilles med mellemrum.
    for($i=0; $i < count($bes); $i++){
    $c=bcmod(bcpow($bes[$i],$e),$n);
    $k_bes .= $c."␣";
    }
    // Den oprindelige besked, den krypteret besked og nøglerne sendes tilbage.
    return array($besked , $k_bes , $d , $e , $n);
    }
    
    // dekrypter() dekrypterer en besked, $bes, ved hjælpe af nøglerne $d og $n.
    function dekrypter($bes , $d, $n){
    // Tallene splittes op i deres blokke i en liste.
    $bes = explode("␣", $bes);
    // Hver blok dekrypteres
    for($i=0; $i < count($bes); $i++){
    $m = bcmod(bcpow($bes[$i],$d),$n);
    // Er tallet under 1000 tilføjes et 0 foran tallet, for at sikre hver
    // blok er på fire cifre og at det kan skrives om til tegn igen.
    if($m < 1000) {
    $m = "0".$m;
    }
    // Fjerner overflødigt 00.
    if($m == "00") {
        $m = NULL;
        }
        // Tallene splittes op, så hvert tal på to cifre, kan omskrives til tegn.
        $m = str_split($m , 2);
        $dek .= $m[0]."␣";
        $dek .= $m[1]."␣";
        }
        $tegn = array("a", "b", "c", "d", "e", "f", "g", "h",
        "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
        "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D",
        "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
        "␣", ".", ",", ":", "-", "/");
        $tal = array("01␣", "02␣", "03␣", "04␣", "05␣", "06␣",
        "07␣", "08␣", "09␣", "10␣", "11␣", "12␣", "13␣", "14␣",
        "15␣", "16␣", "17␣", "18␣", "19␣", "20␣", "21␣", "22␣",
        "23␣", "24␣", "25␣", "26␣", "27␣", "28␣", "29␣", "30␣",
        "31␣", "32␣", "33␣", "34␣", "35␣", "36␣", "37␣", "38␣",
        "39␣", "40␣", "41␣", "42␣", "43␣", "44␣", "45␣", "46␣",
        "47␣", "48␣", "49␣", "50␣", "51␣", "52␣", "53␣", "54␣",
        "55␣", "56␣", "57␣", "58␣");
        $dek = str_replace($tal , $tegn , $dek);
        // Den dekrypteret besked kan nu sendes tilbage.
        return $dek;
        }
?>

    
    
#load "str.cma";;
open Printf;;

let entree = Sys.argv.(1);;
let q = int_of_string Sys.argv.(2);;
let sortie = "clauses.cnf";;

(* Formules logiques *)

type formule =
  |Var of int
  |Non of formule
  |Et of formule * formule
  |Ou of formule * formule;;

let non = function
  |Non f -> f
  |f -> Non f;;

let et f g = Et (f, g);;

let ou f g = Ou (f, g);;

let imp f g = ou (non f) g;;

let equiv f g = et (imp f g) (imp g f);;

(* Simplification en FNC *)

let depl_non f =
  let rec loop f re = match f with
    |Var n -> re (Var n)
    |Et (f, g) ->
      loop f (fun f' ->
          loop g (fun g' ->
              re (Et (f', g'))))
    |Ou (f, g) ->
      loop f (fun f' ->
          loop g (fun g' ->
              re (Ou (f', g'))))
    |Non (x) -> match x with
      |Var n -> re (Non (Var n))
      |Non f -> loop f (fun f' -> re f')
      |Et (f, g) ->
        loop (Non f) (fun f' ->
            loop (Non g) (fun g' ->
                re (Ou (f', g'))))
      |Ou (f, g) ->
        loop (Non f) (fun f' ->
            loop (Non g) (fun g' ->
                re (Et (f', g'))))
  in loop f (fun x -> x);;

let concat x l =
  let rec aux r = function
    |[] -> r
    |h::t -> aux ((h @ x)::r) t
  in aux [] l;;

let produit_concat l1 l2 =
  let rec aux r = function
    |[] -> r
    |h::t -> aux ((concat h l1) @ r) t
  in aux [] l2;;

let fnc f =
  let rec loop f re = match f with
    |Var n -> re [[n]]
    |Et (f, g) ->
      loop f (fun f' ->
          loop g (fun g' ->
              re (f' @ g')))
    |Ou (f, g) ->
      loop f (fun f' ->
          loop g (fun g' ->
              re (produit_concat f' g')))
    |Non f -> match f with
      |Var n -> re [[-n]]
      |_ -> loop (depl_non (Non f)) (fun f' -> re f')
  in loop f (fun x -> x);;

(* Entrée des paramètres *)

let ic = open_in entree;;

let str_to_list s = List.map int_of_string (Str.split (Str.regexp " ") s);;

let param = input_line ic;;
let [n;p] = str_to_list param;;

let add_edges k =
  let rec aux r = function
    |0 -> r
    |k -> let s = input_line ic in
      let [i;j] = str_to_list s in
      aux ((i,j)::r) (k-1)
  in aux [] k;;

let edges = add_edges p;;

close_in ic;;

(* Unicité des couleurs *)

let c i k = q * (i - 1) + k;;

let rec fold f b = function
  |[] -> b
  |h::t -> fold f (f h b) t;;

let range a b =
  let rec aux r a =
    if a > b then r
    else aux (a::r) (a + 1)
  in aux [] a;;

let f i k k' g =
  if k' = k then et (Var (c i k')) g
  else et (non (Var (c i k'))) g;;
let b i k = if k = 1 then Var (c i 1)
  else Non (Var (c i 1));;

let couleur_k k i = fold (f i k) (b i k) (range 2 q);;

let couleur_unique i = fold (fun k f -> ou (couleur_k k i) f) (couleur_k 1 i) (range 2 q);;

let tous_couleur_unique = fold (fun i f -> et (couleur_unique i) f) (couleur_unique 1) (range 2 n);;

(* Couleurs des voisins différentes *)

let meme_couleur (i,j) = fold (fun k f -> et (equiv (Var (c i k)) (Var (c j k))) f) (equiv (Var (c i 1)) (Var (c j 1))) (range 2 q);;

let couleurs_differentes l = fold (fun p f -> et (non (meme_couleur p)) f) (non (meme_couleur (List.hd l))) (List.tl l);;

let conditions = Et (tous_couleur_unique, couleurs_differentes edges);;

let clauses = fnc conditions;;

let longueur = List.length clauses;;

(* Sortie CNF *)

let oc = open_out sortie;;

let ligne l =
  let rec aux r = function
    |[] -> r ^ "0"
    |h::t -> aux (r ^ (string_of_int h) ^ " ") t
  in aux "" l;;

let ecrire_ligne s = fprintf oc "%s\n" s;;

let ecrire_cnf l =
  let rec aux = function
    |[] -> ()
    |h::t -> ecrire_ligne (ligne h); aux t
  in ecrire_ligne ("p cnf " ^ (string_of_int (n*q)) ^ " " ^ (string_of_int longueur));
  aux l;;

let () = ecrire_cnf clauses;;

close_out oc;;

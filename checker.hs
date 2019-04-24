import Data.Maybe


data Tree a b = Leaf a | Node b (Tree a b) (Tree a b) deriving (Show, Read)
data OP = SUM | RES | MUL | DIV deriving (Show, Read)

myRead :: String -> Maybe (Double)
myRead s = case reads s of
    [] -> Nothing
    x -> Just (eval $ getData x)
        where getData ((d,x):xs) = d

eval :: Tree Double OP -> Double
eval (Leaf x) = x
eval (Node SUM x y) = eval x + eval y
eval (Node RES x y) = eval x - eval y
eval (Node MUL x y) = eval x * eval y
eval (Node DIV x y) = eval x / eval y

main = do
    string <- getLine
    putStrLn $ show $ myRead string
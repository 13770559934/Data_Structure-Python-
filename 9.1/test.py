from buildParseTree import buildParseTree;
from buildParseTree import evaluate;
from TreeTraversal import preorder;
from TreeTraversal import postorder;

x = "( ( 3 + 2 ) * ( 5 + 3 ) )";

postorder(buildParseTree(x));
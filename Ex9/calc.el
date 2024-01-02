
LISP


(defun add (x y) (+ x y))

(defun subtract (x y) (- x y))

(defun multiply (x y) (* x y))

(defun divide (x y)
  (if (zerop y)
      "Undefined"
      (/ x y)))

(defun calculator ()
  (format t "Menu:~%")
  (format t "1. Addition~%")
  (format t "2. Subtraction~%")
  (format t "3. Multiplication~%")
  (format t "4. Division~%")
  (format t "5. Exit~%")
  (loop
    (format t "Enter your choice: ")
    (let ((choice (read)))
      (cond
        ((= choice 1)
         (format t "Enter first number: ")
         (let ((num1 (read)))
           (format t "Enter second number: ")
           (let ((num2 (read)))
             (format t "Result: ~a~%" (add num1 num2)))))
        ((= choice 2)
         (format t "Enter first number: ")
         (let ((num1 (read)))
           (format t "Enter second number: ")
           (let ((num2 (read)))
             (format t "Result: ~a~%" (subtract num1 num2)))))
        ((= choice 3)
         (format t "Enter first number: ")
         (let ((num1 (read)))
           (format t "Enter second number: ")
           (let ((num2 (read)))
             (format t "Result: ~a~%" (multiply num1 num2)))))
        ((= choice 4)
         (format t "Enter first number: ")
         (let ((num1 (read)))
           (format t "Enter second number: ")
           (let ((num2 (read)))
             (format t "Result: ~a~%" (divide num1 num2)))))
        ((= choice 5)
         (format t "Exiting calculator. Goodbye!~%")
         (return))
        (t (format t "Invalid choice!~%"))))))


PROLOG


% Addition
add(X, Y, Result) :- Result is X + Y.

% Subtraction
subtract(X, Y, Result) :- Result is X - Y.

% Multiplication
multiply(X, Y, Result) :- Result is X * Y.

% Division
divide(X, Y, Result) :- Y =\= 0, Result is X / Y.
divide(_, 0, 'Undefined').

% Menu for calculator operations
calculator_menu :-
    write('Menu:'), nl,
    write('1. Addition'), nl,
    write('2. Subtraction'), nl,
    write('3. Multiplication'), nl,
    write('4. Division'), nl,
    write('5. Exit'), nl.

% Main calculator program
calculator :-
    repeat,
    calculator_menu,
    write('Enter your choice: '),
    read(Choice),
    (Choice =:= 5 ->
        write('Exiting calculator. Goodbye!'), nl, !;
        (Choice >= 1, Choice =< 4 ->
            write('Enter first number: '),
            read(Number1),
            write('Enter second number: '),
            read(Number2),
            (Choice =:= 1 ->
                add(Number1, Number2, Result),
                format('Result: ~w', [Result]), nl;
            Choice =:= 2 ->
                subtract(Number1, Number2, Result),
                format('Result: ~w', [Result]), nl;
            Choice =:= 3 ->
                multiply(Number1, Number2, Result),
                format('Result: ~w', [Result]), nl;
            Choice =:= 4 ->
                divide(Number1, Number2, Result),
                format('Result: ~w', [Result]), nl;
            write('Invalid choice!'), nl
            ), nl, fail
        )
    ).

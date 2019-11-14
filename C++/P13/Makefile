CXXFLAGS += --std=c++17

debug: CXXFLAGS += -g

all: solution

test: all
	./solution | tee result.txt

solution: P13.cpp
	 $(CXX) $(CXXFLAGS) P13.cpp -o solution

clean:
	-rm -f *.o *.gch *~ a.out solution result.txt


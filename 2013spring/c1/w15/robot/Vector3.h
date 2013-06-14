#pragma once
//Based on libdms OpenGL Toolkit http://resumbrae.com/ub/dms424_s03/libdms/

#include <iostream>
#include <cmath>
#include <GL/glut.h>

class Vector3
    {
    public:
        GLfloat v[3];

        Vector3(void);
        ~Vector3(void);
        Vector3(GLfloat x, GLfloat y, GLfloat z);
        Vector3(const GLfloat *v);
        Vector3(const Vector3 &v);
        Vector3& operator= (const Vector3& v);
        void set(GLfloat x, GLfloat y, GLfloat z);

        GLfloat& operator[](int i);
        GLfloat operator[](int i) const;

        Vector3& operator+=(const Vector3& v);
        Vector3& operator-=(const Vector3& v);
        Vector3& operator*=(GLfloat s);
        Vector3& operator/=(GLfloat s);
        Vector3 operator+(const Vector3& v) const;
        Vector3 operator-(const Vector3& v) const;
        Vector3 operator*(GLfloat s) const;
        Vector3 operator/(GLfloat s) const;
        Vector3 operator-(void) const;
        bool operator==(const Vector3& v) const;
        bool operator!=(const Vector3& v) const;
        
        GLfloat length(void) const;
        GLfloat lengthSquared(void) const;
        void normalize(void);
        GLfloat dot(const Vector3& v) const;
        Vector3 cross(const Vector3& v) const;
        GLfloat distance(const Vector3& v) const;
        GLfloat distanceSquared(const Vector3& v) const;
        GLfloat angle(const Vector3& v) const;
        GLfloat angleSigned( const Vector3& vRef ) const;

        void draw(const Vector3& origin) const;
        char* toString();

        static const Vector3 ZERO;
        static const Vector3 X_AXIS;
        static const Vector3 Y_AXIS;
        static const Vector3 Z_AXIS;

    private:
        char* buffer;

};

inline 		std::ostream& operator<< (std::ostream& s, const Vector3& v)
        { return s << "(" << v.v[0] << ", " << v.v[1] << ", " << v.v[2] << ")"; }


inline Vector3 operator* (GLfloat s, const Vector3& v) { return v*s; }

/****************************************************************************
*                                                                           *
* Texture Loader                                                            *
*                                                                           *
* Originally Based on Jeff Molofee's IPicture Basecode                      *
* Extensions By Chris Leathley (http://members.iinet.net.au/~cleathley/)    *
*                                                                           *
*****************************************************************************
*                                                                           *
*  Loads  : BMP, EMF, GIF, ICO, JPG, WMF and TGA                            *
*  Source : Reads From Disk, Ram, Project Resource or the Internet          *
*  Extras : Images Can Be Any Width Or Height                               *
*           Low Quality Textures can be created                             *
*           Different Filter Level Support (None, Bilinear and Trilinear    *
*           Mipmapping Support                                              *
*                                                                           *
*****************************************************************************
*                                                                           *
*  Free To Use In Projects Of Your Own.  All I Ask For Is A Simple Greet    *
*  Or Mention of my site in your readme or the project itself :)            *
*                                                                           *
*****************************************************************************
*                                                                           *
* Revision History                                                          *
*                                                                           *
* Version 1.0 Released                                                      *
* Version 1.1 Added FreeTexture and LoadTextureFromResource                 *
*			  Added TexType to the glTexture Struction                      *
*             Optimisations to the Alpha Conversion Loop			        *
* Version 1.2 Added Support PSP8 TGA files...                               *
*             Single TGA file loader                                        *
* Version 1.3 Added Support for low quality textures..                      *
*             Added ScaleTGA function                                       *
* Version 1.4 Added Support for gluScaleImage                               *
*             Removed ScaleTGA (replacew with gluScaleImage)                *
*             Added TextureFilter and MipMapping Support                    *
*                                                                           *
****************************************************************************/

#ifndef _TEXTURE_LOADER_H_
#define _TEXTURE_LOADER_H_

#include <windows.h>										// Header File For Windows
#include <gl\gl.h>											// Header File For The OpenGL32 Library
#include <gl\glu.h>											// Header File For The GLu32 Library
#include <olectl.h>											// Header File For The OLE Controls Library
#include <math.h>											// Header File For The Math Library
#include <STDIO.H>											// Header File For I/O Library

// Define Interface Data Types / Structures
//
typedef enum {
	txUnknown	= 0,	// images
	txBmp		= 1,
	txJpg		= 2,
	txPng		= 3,
	txTga		= 4,
	txGif		= 5,
	txIco		= 6,
	txEmf		= 7,
	txWmf		= 8,
	// add new ones at the end
} eglTexType;

typedef enum {
	txNoFilter	= 0,
	txBilinear	= 1,
	txTrilinear	= 2,
	// add new ones at the end
} eglTexFilterType;

typedef	struct
{
	GLuint		TextureID;									// Texture ID Used To Select A Texture
	eglTexType	TexType;									// Texture Format
	GLuint		Width;										// Image Width
	GLuint		Height;										// Image Height
	GLuint		Type;										// Image Type (GL_RGB, GL_RGBA)
	GLuint		Bpp;										// Image Color Depth In Bits Per Pixel
} glTexture;

typedef struct {
	float	s;
	float	t;
} _glTexturCord;


typedef struct {
	_glTexturCord TopRight;
	_glTexturCord TopLeft;
	_glTexturCord BottomLeft;
	_glTexturCord BottomRight;
} glTexturCordTable;

// Define Private Structurs
//

// Header
typedef struct {
	unsigned char ImgIdent;
	unsigned char ignored[ 1 ];
	unsigned char ImgType;
	unsigned char ignored2[ 9 ];
	unsigned char WidthLo;
	unsigned char WidthHi;
	unsigned char HeightLo;
	unsigned char HeightHi;
	unsigned char Bpp;
	unsigned char ignored3[ 1 ];
} _TGAHeader;

// define TextureLoader Class
//
class TextureLoader
{
public:
	// methods
						TextureLoader();
	virtual				~TextureLoader();
	void				SetAlphaMatch(GLboolean fEnabled, GLubyte RedAlphaMatch, GLubyte GreenAlphaMatch, GLubyte BlueAlphaMatch);
	void				SetHighQualityTextures(GLboolean fEnabled);
	void				SetMipMapping(GLboolean fEnabled);
	void				SetTextureFilter(eglTexFilterType type);

	int					LoadTextureFromDisk(char *szFileName, glTexture *pglTexture);
	int					LoadTextureFromRam(unsigned char *pData, int Length, glTexture *pglTexture, eglTexType TexType);
	int					LoadTextureFromResource(unsigned int ResourceName, char *pResourceType, glTexture *pglTexture, eglTexType TexType);
	void				FreeTexture(glTexture *pglTexture);
	// variables

private:
	// methods
	int					BuildTexture(char *szPathName, glTexture *pglTexture);
	int					LoadTGAFromDisk(char *pszFileName, glTexture *pglTexture);

	int					LoadJPG_GIFResource(char *pResourceName, char *pResourceType, glTexture *pglTexture);
	int					LoadTGAResource(char *pResourceName, char *pResourceType, glTexture *pglTexture);

	int					GenerateTexture(glTexture *pglTexture, GLubyte *pImgData);

	void				ExtensionFromFilename(char *szFileName, char *szExtension);

	// variables
	GLboolean			m_fAlphaConversion;
	GLboolean			m_fHighQualityTextures;
	GLboolean			m_fMipMapping;
	eglTexFilterType	m_TextureFilterType;

	GLubyte				m_RedAlphaMatch;
	GLubyte				m_GreenAlphaMatch;
	GLubyte 			m_BlueAlphaMatch;
};

#endif // _TEXTURE_LOADER_H_

